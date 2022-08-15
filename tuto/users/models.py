from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username, email, name, password, is_staff,
                    is_superuser, **extra_fields):
        user = self.model(
            username=username,
            email=email,
            name=name,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, username, email, name, password=None,
                         **extra_fields):
        return self.create_user(username, email, name, password, True,
                                 True, **extra_fields)


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
    REQUIRED_FIELDS = ['email', 'name']

    def __str__(self):
        return f'{self.name},{self.last_name}'


class Student(models.Model):

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name=('Usuario')
    )
    code = models.CharField(
        verbose_name="Código", max_length=20, unique=True, blank=False, null=False
    )
    phone_number = models.CharField(
        verbose_name="Número de teléfono", max_length=20, blank=True, null=True
    )
    address = models.CharField(
        verbose_name="Dirección", max_length=100, blank=True, null=True
    )
    photo = models.ImageField(
        upload_to='foto_estudiante/',
        blank=True, null=True, verbose_name=('Foto')
    )

    class Meta:
        verbose_name = ('Estudiante')
        verbose_name_plural = ('Estudiantes')

    def __str__(self):
        return self.user.name


class Teacher(models.Model):

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name=('Usuario')
    )
    document = models.CharField(
        verbose_name="Código", max_length=20, unique=True, blank=False, null=False
    )
    phone_number = models.CharField(
        verbose_name="Número de teléfono", max_length=20, blank=True, null=True
    )
    address = models.CharField(
        verbose_name="Dirección", max_length=100, blank=True, null=True
    )
    photo = models.ImageField(
        upload_to='foto_profesor/',
        blank=True, null=True, verbose_name=('Foto')
    )

    class Meta:
        verbose_name = ('Profesor')
        verbose_name_plural = ('Profesores')

    def __str__(self):
        return self.user.name