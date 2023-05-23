from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, PermissionsMixin, BaseUserManager
from django.contrib.auth import get_user_model





### CustomAccount
class CustomAccountManager(BaseUserManager):

    def create_superuser(self, username, email, Name, Phone, password, **other_fields):

        if not username:
            raise ValueError(_('You must provide an username'))

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        user = self.model(username=username, email=None, Name=Name, Phone=Phone, password=password, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, username,password,Phone, Name, **other_fields):

        if not Phone:
            raise ValueError(_('You must provide a Phone number'))

        #email = self.normalize_email(email)
        user = self.model(username=username,password=password, Phone=Phone, Name=Name, **other_fields)
        user.set_password(password)
        user.save()
        return user



### User mode...
class SystemUser(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=100, unique=True, null=True, blank=True)
    email = models.EmailField(_('email address'), null=True, blank=True)
    Phone = models.CharField(max_length = 16, unique=True, null=False, blank=False)
    Name = models.CharField(max_length=150, null=False, blank=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = CustomAccountManager()
    

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['Name', 'Phone', 'email']
   
    def __str__(self):
        return f"{self.Name} ({self.Phone})"
    
    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

### Profile model...
class Profile(models.Model):

    user = models.OneToOneField(SystemUser, on_delete = models.CASCADE)
    profile_pic = models.FileField()
    bio = models.TextField(null=True,blank=True)
    othersitelink = models.TextField(null=True,blank=True)

    def __str__(self):
        return f'{self.id} {self.user}'
