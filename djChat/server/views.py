from .models import Server
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.exceptions import AuthenticationFailed, ValidationError
from rest_framework.response import Response
from .serializer import ServerSerializer, CategorySerializer
from .schema import server_list_docs
from django.db import models


# Define a viewset for listing servers
class ServerListViewSet(ViewSet):
    queryset = Server.objects.all()

    # Define the list method to handle GET requests
    @server_list_docs
    def list(self, request):
        """
        Handle GET requests to retrieve a list of servers with optional filtering and annotations.

        Query Parameters:
        - category (str): Filter servers by category name.
        - qty (int): Limit the number of servers returned.
        - by_user (bool): If 'true', filter servers by the authenticated user's membership.
        - by_serverid (int): Filter servers by a specific server ID.
        - with_num_members (bool): If 'true', include the number of members in each server.

        Authentication:
        - Required if filtering by 'by_user' or 'by_serverid'.

        Raises:
        - AuthenticationFailed: If the user is not authenticated and filtering by user or server ID.
        - ValidationError: If the server ID is invalid or not found.

        Returns:
        - Response: Serialized data of servers, optionally including the number of members.
        """
        category = request.query_params.get("category")
        qty = request.query_params.get("qty")
        by_user = request.query_params.get("by_user") == "true"
        by_serverid = request.query_params.get("by_serverid")
        with_num_members = request.query_params.get("with_num_members") == "true"

        # Check authentication if filtering by user or server ID
        if not request.user.is_authenticated and (by_serverid or by_user):
            raise AuthenticationFailed("Authentication Failed")

        # Filter queryset by category if specified
        if category:
            self.queryset = self.queryset.filter(category__name=category)

        # Filter queryset by the authenticated user if specified
        if by_user and request.user.is_authenticated:
            self.queryset = self.queryset.filter(member=request.user.id)

        # Annotate queryset with the number of members if requested
        if with_num_members:
            self.queryset = self.queryset.annotate(num_members=models.Count("member"))

        if qty:
            self.queryset = self.queryset[: int(qty)]

        if by_serverid:
            try:
                server_id = int(request.query_params.get("by_serverid"))
                self.queryset = self.queryset.filter(id=server_id)
                if not self.queryset.exists():
                    raise ValidationError(
                        detail=f"Server with id {by_serverid} not Found"
                    )
            except ValueError:
                raise ValidationError(detail="Server Value Error")

        # Serialize the queryset and include the number of members if requested
        serializer = ServerSerializer(
            self.queryset, many=True, context={"num_members": with_num_members}
        )
        # Return the serialized data in the response
        return Response(serializer.data)
