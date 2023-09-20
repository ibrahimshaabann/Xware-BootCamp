from django.shortcuts import render
from rest_framework import viewsets, filters

from NotificationsApp.permissions import RolePermissions
from .models import Notifications, User
from NotificationsApp.serializers import NotificationsSerializer


from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
import jwt
from django.conf import settings


class CustomAuthentication(BaseAuthentication):
    """
    Custom authentication class that uses JWT tokens for user authentication.

        This authentication class is responsible for verifying JWT tokens provided in the
        Authorization header of the incoming HTTP request. It decodes the token, extracts
        the user ID from the payload, and retrieves the corresponding user object from
        the database. If the token is valid and the user exists, the authentication is
        considered successful. Otherwise, the authentication fails.

    Attributes:
        None

    Methods:
        authenticate(request): Authenticate the user based on the JWT token.
    """

    def authenticate(self, request): 
        """
        Authenticate the user based on the provided JWT token.

        Args:
            request (HttpRequest): The incoming HTTP request.

        Returns:
            tuple: A tuple containing the authenticated user object and metadata.

        Raises:
            AuthenticationFailed: If the JWT token is invalid or the user does not exist.
        """

         # Get the Authorization header from the request
        header :str = request.META.get('HTTP_AUTHORIZATION')
        if not header:
            """
                The first None value corresponds to the user object, 
                the second None value corresponds to any additional authentication metadata. 
                Since the authentication has failed, there is no valid user object or authentication metadata to return.
            """
            return None, None
        
        try:
            parts = header.split()
            # Decode the JWT token using the provided secret key and specified algorithm
            payload = jwt.decode(
                parts[1],                   # The second part of the JWT (the token itself)
                settings.SECRET_KEY,        # The secret key used for decoding
                algorithms="HS256"          # The algorithm used for encoding and decoding (HMAC-SHA256)
            )

            payload_user_id = payload['user_id']
            user = User.objects.filter(pk= payload_user_id).first()
            if not user:
                raise AuthenticationFailed
            return user, payload

        except Exception as e:
            print(e)
            raise AuthenticationFailed


from rest_framework.request import Request
from django.contrib.auth import authenticate
from rest_framework.exceptions import NotFound, APIException
from rest_framework.response import Response
from rest_framework.views import APIView

class TokenView(APIView): 
    """
    API view to authenticate users and generate JWT tokens.

    This view is responsible for authenticating users based on their username and password.
    If the authentication is successful, it generates a JWT token containing the user's
    ID and returns it as a response.

    Attributes:
        None

    Methods:
        post(request): Authenticate user and generate JWT token.
    """

    def post(self, request :Request):
        """
        Authenticate user and generate a JWT token.

        Args:
            request (Request): The incoming HTTP request.

        Returns:
            Response: A JSON response containing the generated JWT token.

        Raises:
            NotFound: If the provided username and password combination is not found.
            APIException: If an unspecified exception occurs during the authentication process.
        """
        try:
            # Extract username and password from the request data
            retrieved_username = request.data.get('username')
            retrieved_password = request.data.get('password')

            
            # >>> Note to create user with this command User.objects.create_user(username = "koko" , password = "123") 
            # Authenticate the user with the provided credentials
            user = authenticate(username=retrieved_username, password=retrieved_password)
            print(retrieved_username)
            print(retrieved_password)
            print(f"\n\n\n\n alo \n\n\n\n")

            if not user:
                raise NotFound("Invalid usernamer or password")

            # Generate a JWT token with the user's ID as the payload
            generated_token = jwt.encode(
                {'user_id': user.pk},
                settings.SECRET_KEY,
                algorithm='HS256'
                )
   
            return Response({'token':generated_token})

        except Exception as e:
            raise APIException ("An error occured during authentication")




from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser


class NotificationsModelViewSet(viewsets.ModelViewSet):
    """
        authentication classes: El server by3raf enta meen
        permission classes: El permissions bta3et kol wahed meen y2dar yeshof eh w meen my2darsh yshof eh
    """
    permission_classes=[RolePermissions] 
    authentication_classes=[CustomAuthentication]
    serializer_class = NotificationsSerializer
    queryset = Notifications.objects.all()
    
    

# Create your views here.
