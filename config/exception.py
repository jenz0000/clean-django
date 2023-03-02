# built-in
import traceback

# django
from django.conf import settings

# djangorestframework
from rest_framework import status
from rest_framework.exceptions import APIException

# project
from config.constants import CODE
from config.response import create_response


def global_exception_handler(exc, context):
    request = context["request"]
    response = api_exception_handler(exc, context, request)
    if response:
        return response

    if settings.DEBUG:
        traceback.print_exc()

    return create_response(
        status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        code=CODE.UNKNOWN_SEVER_ERROR,
    )


def api_exception_handler(exc, context, request):
    if not isinstance(exc, APIException):
        return None

    payload = {
        "data": getattr(exc, "data", {}),
        "code": getattr(exc, "code", CODE.INVALID_PARAMETERS),
        "status": getattr(exc, "status_code", status.HTTP_400_BAD_REQUEST),
    }

    return create_response(**payload)


class ApiException(APIException):
    def __init__(self, **kwargs):
        self.status_code = kwargs.get("status", status.HTTP_400_BAD_REQUEST)
        self.code = kwargs.get("code", CODE.INVALID_PARAMETERS)
        self.data = kwargs.get("data", {})
        self.detail = kwargs.get("detail", "")
