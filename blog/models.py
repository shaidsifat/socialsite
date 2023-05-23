from django.db import models
from accounts.models import SystemUser
from django.utils import timezone
# Create your models here.

class Blog(models.Model):

    text = models.TextField()
    image = models.FileField()
    like = models.PositiveIntegerField(null=True,blank=True)
    comment = models.PositiveIntegerField(null=True,blank=True)
    share = models.PositiveIntegerField(null=True,blank=True)
    created_by = models.ForeignKey(SystemUser,on_delete = models.CASCADE,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):

        return self.id


