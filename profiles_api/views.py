from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework import viewsets
from . import serializers,models,permissions

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



class HelloViewSet(viewsets.ViewSet):

    """ test API viewset"""
    serializer_class=serializers.HelloSerializer
    def list(self,request):
        a_viewset=['view set is ease than APIView ','and not simple']
        return Response({'message':'hello','a_viewset':a_viewset})

    def create(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        """ Handle getting an object by it's ID"""
        return Response({'http_method':'GET'})

    def update(self,request,pk=None):
        return Response({'http_method':"PUT"})

    def partial_update(self,request,pk=None):
        return Response({'http_method':"PATCH"})

    def destroy(self,request,pk=None):
        return Response({'http_method':"DELETE"})           

class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class=serializers.UserProfileSerializer
    queryset=models.UserProfile.objects.all()
    authentication_classes=(TokenAuthentication,)
    permission_classes=(permissions.UpdateOwnProfile,)
    filter_backends=(filters.SearchFilter,)
    search_fields=('name','email',)


class UserLoginApiView(ObtainAuthToken):
    """ handle creating  user  authentication tokens"""
    renderer_classes=api_settings.DEFAULT_RENDERER_CLASSES    


