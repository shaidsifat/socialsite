from django.contrib import admin
from .models import (
    SystemUser,
    Profile,
    )

# Register your models here.
admin.site.register(SystemUser)
admin.site.register(Profile)