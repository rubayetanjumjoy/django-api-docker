from user.models import User
from django.test import TestCase,Client
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework_simplejwt.tokens import RefreshToken

# testing get url
# class APIView(TestCase):
#     # initialize test
 
#     def setUp(self):
#         """Test creating a new user"""
#         self.client = Client()
        
#         password = 'testpass123'
#         email = 'testuser@aascom'
#         user = User.objects.create_user(
            
#             email=email,
#             password=password
#         )
#         # Get the access token
#         token = RefreshToken.for_user(user)
#         headers = {'Authorization': f'Bearer {token}'}
#         url=reverse('user-list')
#         response = self.client.get(url, headers=headers)
#         print(response.data)
#         self.assertEqual(user.email, email)
#         self.assertTrue(user.check_password(password))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)


    
    def test_api_respons_check(self):
    
        url = reverse('user-list')
        
        response=self.client.get(url)
        
        

        self.assertEqual(response.status_code, status.HTTP_200_OK)

   
    

