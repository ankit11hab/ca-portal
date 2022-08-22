

from django.db import models
import uuid
from django.utils import timezone
from datetime import datetime

# Create your models here.


class ShareablePost(models.Model):
    id = models.SlugField(primary_key=True, default=uuid.uuid4)
    link_instagram = models.CharField(max_length=500, blank=True, null=True)
    link_facebook = models.CharField(max_length=500, blank=True, null=True)
    is_instagram = models.BooleanField(default=False)
    is_facebook = models.BooleanField(default=False)
    media_id = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to="image-uploads/")
    caption = models.CharField(max_length=160)
    created_on = models.DateTimeField(default=timezone.now)
    last_date = models.DateTimeField(default=timezone.now)
    likedusers = models.TextField(default = '', null=True,blank=True)

    @property
    def getLastdate(self):
     if self.last_date:
        return (self.last_date.replace(tzinfo=None)-datetime(1970,1,1)).total_seconds()

    def __str__(self):
        return str(self.id)

class Promotions(models.Model):
    id = models.SlugField(primary_key=True, default=uuid.uuid4)
    link = models.CharField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to="image-uploads/")
    description = models.TextField(default = '', null=True,blank=True)
    created_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.id)


class Notifications(models.Model):
    TYPECHOICES = [
        ('Success', 'Success'),
        ('Warning', 'Warning'),
        ('Info', 'Info'),
    ]
    id = models.SlugField(primary_key=True, default=uuid.uuid4)
    message = models.CharField(max_length=200)
    user = models.ForeignKey(
        'users.NewUser', default=None, null=True,blank=True, on_delete=models.CASCADE)
    created_on = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=200,choices=TYPECHOICES)
    isread=models.BooleanField(default=False)
    def __str__(self):
        return str(self.id)
