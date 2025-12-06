from django.db import models
#
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager, models.Manager):

    def _create_user(self, email, nombre, apellido, password, is_active, is_staff, is_superuser, **extra_fields):
        user = self.model(
            email = email,
            nombre = nombre,
            apellido = apellido,
            is_active = is_active,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user


    def create_user(self, email, nombre, apellido, password=None, **extra_fields):
        return self._create_user(email, nombre, apellido, password, False, False, False, **extra_fields)


    def create_superuser(self, email, nombre, apellido, password=None, **extra_fields):
        return self._create_user(email, nombre, apellido, password, True, True, True, **extra_fields)