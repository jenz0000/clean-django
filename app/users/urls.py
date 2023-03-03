# django
from django.urls import path

# app.user
from app.users.views import UserViewSet

urlpatterns = [path("api/users/", UserViewSet.as_view({"post": "create"}))]
