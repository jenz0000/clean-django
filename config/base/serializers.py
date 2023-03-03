# djangorestframework
from rest_framework import serializers


class BaseSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs) -> None:
        fields = kwargs.pop("fields", [])

        super().__init__(*args, **kwargs)

        for field in self.fields:
            if field not in fields:
                self.fields[field].required = False
