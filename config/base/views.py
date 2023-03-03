# built-in
import abc
from typing import Dict

# django
from django.http import HttpRequest, HttpResponse

# djangorestframework
from rest_framework import viewsets, status

# project
from config.constants import MESSAGE
from config.exception import ApiException
from config.base.serializers import BaseSerializer


class BaseViewSet(viewsets.ViewSet, abc.ABC):
    @property
    @abc.abstractmethod
    def serializer(self) -> BaseSerializer:
        pass

    def validate_request(self, request: HttpRequest, **kwargs) -> bool:
        fields = kwargs.get("fields", [])

        self.serializer = self.serializer(data=request.data, fields=fields)
        if not self.serializer.is_valid():
            raise ApiException(code=MESSAGE.INVALID_FORMAT)

        self.data = self.serializer.validated_data

        return True
