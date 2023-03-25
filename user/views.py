from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .serializers import UserSerializer

  
class UserList(APIView):
    # permission_classes = (IsAuthenticated, )
  
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        


        content = {'message': 'Hello, xyz'}
        return Response(data=serializer.data)