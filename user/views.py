from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
import jwt
from django.http import request


  
class UserList(APIView):
   
    authentication_classes = (JWTAuthentication,)

    permission_classes = (IsAuthenticated, )
  
    def get(self, request):
        auth_header = request.GET.get('access')
        print(auth_header)
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        


        content = {'message': 'Hello, xyz'}
        return Response(data=serializer.data)
    
class SingleUser(APIView):
   
    authentication_classes = (JWTAuthentication,)

    permission_classes = (IsAuthenticated, )
  
    def get(self, request):
        
        


        content = {'message': 'Hello, xyz'}
        return Response(content)
    

class UserViewSet(viewsets.ModelViewSet):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    