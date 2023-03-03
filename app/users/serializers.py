# djangorestframework
from rest_framework import serializers

# config
from config.base.serializers import BaseSerializer

# app.user
from app.users.models import User


class UserSerializer(BaseSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "password", "nickname"]

    email = serializers.EmailField()
    password = serializers.CharField(min_length=5, write_only=True)
    nickname = serializers.CharField(min_length=2, max_length=15)

    def validate_nickname(self, data: str) -> str:
        if "admin" in data:
            raise serializers.ValidationError()

        return data
