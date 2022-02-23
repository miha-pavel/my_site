from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class User(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=1024)
    zip_code = models.CharField(max_length=5, default="49010",
        validators=[RegexValidator(
            regex=r'^\d{5}$',
            message='Must be valid zipcode in formats from 00000 to 99999',
        )]
    )
    phone = models.CharField(max_length=1024)