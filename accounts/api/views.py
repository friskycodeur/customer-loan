from .serializers import UserSerializer, RegisterSerializer
from ..models import User
from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.backends import TokenBackend
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.status import (
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
)
from django.core.exceptions import ValidationError


def get_tokens_for_user(user):

    """
    Function that returns the refresh and access token for user.
    """

    refresh = RefreshToken.for_user(user)

    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }


def get_user_from_token(request):

    """
    Function that returns the user from access token.
    """

    token = request.META.get("HTTP_AUTHORIZATION", " ").split(" ")[1]
    data = {"token": token}
    try:
        valid_data = TokenBackend(algorithm="HS256").decode(
            token, verify=False
        )
        user = valid_data["user"]
        request.user = user
    except ValidationError as v:
        print("validation error", v)


class RegisterAPIView(generics.ListCreateAPIView):

    """
    A view that handles User Registration.
    """

    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = "__all__"

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class UserDetail(generics.RetrieveAPIView):

    """
    A view that returns user details from email.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def retrieve(self, request, username):
        queryset = User.objects.filter(username=username)
        user = get_object_or_404(queryset, username=username)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class login(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if not user:
            return Response(
                {"error": "Invalid Credentials"}, status=HTTP_404_NOT_FOUND
            )
        token = get_tokens_for_user(user)
        serializer = UserSerializer(user)
        data = serializer.data
        return Response({"data": data}, status=HTTP_200_OK)
