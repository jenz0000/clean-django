# django
from django.http import HttpRequest

# djangorestframework
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

# project
from config.constants import MESSAGE


def create_response(**kwargs) -> Response:
    headers = kwargs.get("headers", None)
    status_code = kwargs.get("status", status.HTTP_200_OK)

    data = kwargs.get("data", {})
    message = kwargs.get("message", MESSAGE.SUCCESS)

    response = {}
    response["data"] = data
    response["message"] = message
    response["success"] = message == MESSAGE.SUCCESS

    return Response(response, status=status_code, headers=headers)
