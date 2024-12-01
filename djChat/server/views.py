from django.shortcuts import render
from .models import Server
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from .serializer import ServerSerializer , CategorySerializer
# Create your views here.


class ServerListViewSet(ViewSet):
    queryset = Server.objects.all()
    def list(self, request):
        category = request.query_params.get('category')
        qty = request.query_params.get('qty')
        if category:
            self.queryset = self.queryset.filter(category__name=category)
            
        if qty:
            self.queryset = self.queryset[:int(qty)]   # slicing the queryset 

        serializer = ServerSerializer(self.queryset, many=True)
        return Response(serializer.data)