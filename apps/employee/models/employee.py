import uuid

from django_extensions.db.models import TimeStampedModel
from django.db import models
from apps.employee.utils.email_field import EmailField
from .department import Department


class Employee(TimeStampedModel):
    name = models.CharField(max_length=200)
    email = EmailField(max_length=254, unique=True)
    department = models.ForeignKey(
        Department, on_delete=models.PROTECT, related_name='employees'
    )
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
