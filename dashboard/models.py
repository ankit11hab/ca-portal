from django.db import models
import uuid
from django.utils import timezone
# Create your models here.


class ShareablePost(models.Model):
    id = models.SlugField(primary_key=True, default=uuid.uuid4)
    link = models.CharField(max_length=500, unique=False)
    last_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.id)
