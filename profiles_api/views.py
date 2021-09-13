from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status
from . import serializers

class HelloApiView(APIView):
    """ test Api view """
    serializer_class=serializers.HelloSerializer

    def get(self,request,format=None):
        """ Returns  a list of APIView features """
        api_view={'api view so easy and fast'}
        return Response({'message':api_view})

    def post(self,request):
        """ create a Hello message with our name """
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)       


    def put(self,request,pk=None):
        """ updateting an objects """ 
        return Response({'method':'PUT'})

    def patch(self,request,pk=None):
        """ handle a partial update of an objects """ 
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        """ Delete an objects"""
        return Response({'method':'DELETE'})       
