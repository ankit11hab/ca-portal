
from django.db import models
import uuid
from django.utils import timezone
# Create your models here.


class ShareablePost(models.Model):
    id = models.SlugField(primary_key=True, default=uuid.uuid4)
    link_instagram = models.CharField(max_length=500, unique=False)
    link_facebook = models.CharField(max_length=500, unique=False)
    is_instagram = models.BooleanField(default=False)
    is_facebook = models.BooleanField(default=False)
    image = models.ImageField(upload_to="image-uploads/post-images/")
    caption = models.CharField(max_length=160, unique=False)
    created_on = models.DateTimeField(default=timezone.now)
    last_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.id)
