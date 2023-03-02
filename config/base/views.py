# built-in
import abc
from typing import Dict

# django
from django.http import HttpRequest, HttpResponse

# djangorestframework
from rest_framework import viewsets, status

# project
from config.constants import CODE
from config.exception import ApiException
from config.base.serializers import BaseSerializer


class BaseViewSet(viewsets.ViewSet, abc.ABC):
    @property
    @abc.abstractmethod
    def serializer(self) -> BaseSerializer:
        pass

    def validate_request(self, request: HttpRequest, **kwargs) -> Dict:
        required_fields = kwargs.get("required_fields", [])

        serializer = self.serializer(data=request.data, required_fields=required_fields)
        if not serializer.is_valid():
            raise ApiException(code=CODE.INVALID_FORMAT)

        return serializer.validated_data
