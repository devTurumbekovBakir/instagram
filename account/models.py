from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone = models.CharField(max_length=12, null=True, blank=True)


# class Author(models.Model):
#     about = models.TextField()
#     birth_date = models.DateField()
