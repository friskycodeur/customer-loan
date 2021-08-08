from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from accounts.managers import UserManager


ROLE_CHOICES = (("nursery", "Nursery"), ("buyer", "Buyer"))


class User(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(
        unique=True,
        blank=False,
        error_messages={
            "unique": "A user with that email already exists.",
        },
    )
    age = models.PositiveIntegerField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = PhoneNumberField()
    REQUIRED_FIELDS = ["email"]

    def __unicode__(self):
        return self.email

    objects = UserManager()
