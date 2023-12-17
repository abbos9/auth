from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='users/', blank=True, null=True)
    job = models.CharField(max_length=255, blank=True, null=True)
    about_me = models.TextField()
