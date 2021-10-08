
from django.db import models
import uuid
from django.utils import timezone
# Create your models here.


class ShareablePost(models.Model):
    id = models.SlugField(primary_key=True, default=uuid.uuid4)
    link_instagram = models.CharField(max_length=500, blank=True, null=True)
    link_facebook = models.CharField(max_length=500, blank=True, null=True)
    is_instagram = models.BooleanField(default=False)
    is_facebook = models.BooleanField(default=False)
    image = models.ImageField(upload_to="image-uploads/")
    caption = models.CharField(max_length=160)
    created_on = models.DateTimeField(default=timezone.now)
    last_date = models.DateTimeField(default=timezone.now)

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
    user = models.ManyToManyField('users.NewUser')
    created_on = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=200,choices=TYPECHOICES)
    def __str__(self):
        return str(self.id)
