# django
from django.http import HttpRequest

# djangorestframework
from rest_framework import status
from rest_framework.response import Response

# config
from config.constants import MESSAGE
from config.base.views import BaseViewSet
from config.response import create_response

# app.user
from app.users.models import User
from app.users.serializers import UserSerializer


class UserViewSet(BaseViewSet):
    serializer = UserSerializer

    def create(self, request):
        self.validate_request(request, fields=["email", "password", "nickname"])

        data = self.data

        user = User.objects.create_user(
            email=data["email"],
            password=data["password"],
            nickname=data["nickname"],
        )

        return create_response(data=UserSerializer(user).data, status=status.HTTP_201_CREATED)
