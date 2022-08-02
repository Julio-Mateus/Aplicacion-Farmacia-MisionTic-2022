from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    def create_user(self, username, password = None):
        if not username:
            raise ValueError('Es necesario el nombre de usuario')
        elif not password:
            raise ValueError('Es necesario el password')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, username, password = None):
        user = self.create_user(username = username, password = password)
        user.is_admin = True
        user.save(using = self._db)
        return user

class User(AbstractBaseUser,PermissionsMixin):
    identificacion = models.BigIntegerField(primary_key=True, default= 1)
    nombre = models.CharField('Nombre', max_length=50, default="")
    apellido = models.CharField('Apellido', max_length=150, default="")
    username = models.CharField('UserName', max_length=255, unique=True)
    password = models.CharField('Password', max_length=255, unique=True)
    email = models.EmailField('Email', max_length=200)

    def save(self, **kwargs):
        some_salt = 'dh74gygbhvggv'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)

    objects = UserManager()
    USERNAME_FIELD = 'username'