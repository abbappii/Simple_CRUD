from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=100, blank=True)
    zip_code = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    email = models.EmailField(unique=True, db_index=True)

    class Meta:
        ordering = ("-date_joined",)

    def __str__(self) -> str:
        return f"ID: {self.id} - Name:{self.first_name}"
