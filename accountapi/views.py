from django.contrib.auth import authenticate

# Create your views here.
from rest_framework import generics, status, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView

from accountapi.Serializer import UserSerializer


class UserCreate(generics.CreateAPIView):
    """
    POST auth/login/
    """
    serializer_class = UserSerializer


class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username", )
        password = request.data.get("password", )
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)


class GetUserDetails(APIView):

    def get(self, request, *args, **kwargs):
        user = UserSerializer(request.user)
        return Response(user.data)


class Logout(APIView):
    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response({"message": "logged out", "status": "true"}, status=status.HTTP_200_OK)
