from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


"""
    Note that the User Model inherits from the AbstractUser Model
    , so we create Our User model to custom our needs
"""
class User(AbstractUser):

    class Roles(models.TextChoices):
        SUPERUSER = 'superuser', 'SuperUser'  #----> the left is stored in database and the right is showed to the user
        ADMIN = 'admin', 'Admin'
        USER = 'user', 'User'

    role = models.TextField(
choices=Roles.choices,
        null=False,
        default=Roles.USER
    )



class Notifications(models.Model):
    user = models.ForeignKey(
        get_user_model(), 
        null=True,
        on_delete=models.SET_NULL
    )
    title = models.CharField (max_length=30, null=False)
    body = models.TextField(max_length=200, null=False, default='')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
# Create your models here.
