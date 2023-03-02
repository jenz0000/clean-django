# buit-in
import jwt
import datetime
import functools

# django
from django.conf import settings
from django.contrib.auth.models import User

# djangorestframework
from rest_framework import status
from rest_framework.authentication import BaseAuthentication

# project
from config.constants import CODE, TOKEN
from config.exception import ApiException


class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        authorization_header = request.headers.get("Authorization")
        if not authorization_header:
            return (None, None)

        try:
            access_token = authorization_header.split(" ")[1]  # "Bearer xxxxxxx"
            payload = jwt.decode(access_token, settings.SECRET_KEY, algorithms="HS256")
        except jwt.ExpiredSignatureError:
            return (None, None)
        except jwt.DecodeError:
            return (None, None)

        user = User.objects.filter(id=payload["id"], email=payload["email"]).first()
        if not user:
            return (None, None)

        return (user, None)


def generate_token(user: User, expire_time):
    payload = {
        "id": user.id,
        "email": user.email,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=expire_time),
        "iat": datetime.datetime.utcnow(),
    }

    token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")

    return token


def auth_required(f):
    @functools.wraps(f)
    def wrap(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise ApiException(code=CODE.AUTH_REQUIRED, status=status.HTTP_401_UNAUTHORIZED)

        return f(self, request, *args, **kwargs)

    return wrap
