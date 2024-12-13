from django.shortcuts import render
from .models import Server
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.exceptions import AuthenticationFailed, ValidationError
from rest_framework.response import Response
from .serializer import ServerSerializer , CategorySerializer
from django.db import models
# Create your views here.


class ServerListViewSet(ViewSet):
    queryset = Server.objects.all()
    def list(self, request):
        category = request.query_params.get('category')
        qty = request.query_params.get('qty')
        by_user = request.query_params.get('by_user') == 'true'   
        by_serverid = request.query_params.get('by_serverid')   
        with_num_members = request.query_params.get('with_num_members') == 'true'

        if not request.user.is_authenticated and ( by_serverid or by_user ):
            raise AuthenticationFailed('Authentication Failed')

        if category:
            self.queryset = self.queryset.filter(category__name=category)

        if by_user and request.user.is_authenticated:
        # if request.user.is_authenticated:
            self.queryset = self.queryset.filter(member=request.user.id)


        #  for getting members number also in data 
        if with_num_members:
            self.queryset = self.queryset.annotate(num_members=models.Count('member'))

        if qty:
            self.queryset = self.queryset[:int(qty)]   # slicing the queryset 

        if by_serverid:
            try:
                server_id = int(request.query_params.get('by_serverid'))
                self.queryset = self.queryset.filter(id=server_id)
                if not self.queryset.exists():
                    raise ValidationError(detail=f'Server with id {by_serverid} not  Found')
            except ValueError:
                raise ValidationError(detail='Server Value Error ')

        serializer = ServerSerializer(self.queryset, many=True, context={"num_members":with_num_members})
        return Response(serializer.data)
    