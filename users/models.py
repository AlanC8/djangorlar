from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from abstracts.models import AbstractSoftDeletableModel
from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin, AbstractSoftDeletableModel): 
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(default=timezone.now)
    
    is_staff = models.BooleanField(default=False) 
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.email