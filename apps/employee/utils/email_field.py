from django.db import models


class EmailField(models.EmailField):
    def get_prep_value(self, value):
        value = super(EmailField, self).get_prep_value(value)
        if value is not None:
            value = value.lower()
        return value
