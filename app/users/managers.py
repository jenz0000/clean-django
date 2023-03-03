# django
from django.db import IntegrityError
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _

# config
from config.constants import MESSAGE
from config.exception import ApiException


class UserManager(BaseUserManager):
    def create_user(self, email, password, nickname, **extra_fields):
        user = self.model(email=email, nickname=nickname, **extra_fields)
        user.set_password(password)

        try:
            user.save()
        except IntegrityError as e:
            e = str(e)

            if "email" in e:
                raise ApiException(message=MESSAGE.EMAIL_ALREADY_IN_USE)
            elif "nickname" in e:
                raise ApiException(message=MESSAGE.NICKNAME_ALREADY_IN_USE)

        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        return self.create_user(email, password, **extra_fields)
