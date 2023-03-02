# djangorestframework
from rest_framework import serializers


class BaseSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs) -> None:
        required_fields = kwargs.pop("required_fields", [])

        super().__init__(*args, **kwargs)

        for field in self.fields:
            if field not in required_fields:
                self.fields[field].required = False
