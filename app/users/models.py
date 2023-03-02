# django
from django.db import models
from django.contrib.auth.models import AbstractUser

# project
from config.base.models import BaseModel
from app.users.managers import UserManager


class User(AbstractUser, BaseModel):
    objects = UserManager()

    username = None
    first_name = None
    last_name = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    email = models.EmailField(unique=True)

    class Meta:
        db_table = "user"
        app_label = "users"

    def __str__(self):
        return self.email
