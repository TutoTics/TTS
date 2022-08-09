from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username, email, name, last_name, password=None):
        if not email:
            raise ValueError('El usuario debe tener correo electrónico!')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            name=name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, username, email, name, last_name,
                         password):
        user = self.create_user(
            email,
            username=username,
            name=name,
            last_name=last_name,
        )
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField('Correo Electrónico', max_length=255,
                              unique=True,)
    name = models.CharField('Nombres', max_length=255, blank=True,
                            null=True)
    last_name = models.CharField('Apellidos', max_length=255, blank=True,
                                 null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name', 'last_name']

    def __str__(self):
        return f'{self.name},{self.last_name}'
