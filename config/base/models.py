# django
from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def change(self, **kwargs):
        for field, value in kwargs.items():
            setattr(self, field, value)

        self.save(update_fields=kwargs)
