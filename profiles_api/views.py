from rest_framework.views import APIView 
from rest_framework.response import Response

class HelloApiView(APIView):
    """ test Api view """

    def get(self,request,format=None):
        """ Returns  a list of APIView features """
        api_view={'api view so easy and fast'}
        return Response({'message':api_view})
