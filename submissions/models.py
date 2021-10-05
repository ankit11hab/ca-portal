from django.db import models
from django.urls import reverse
from django.db.models.signals import post_save
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.



class Submission(models.Model):
    is_verified= models.BooleanField(default=False)
    user = models.ForeignKey(User,related_name="%(class)s_submissions",on_delete=models.CASCADE)

class POC(Submission):
    name = models.CharField(max_length=70)
    design = models.CharField(max_length=60)
    college = models.CharField(max_length=90)
    contact = models.CharField(max_length=13)
    submit_date = models.DateField(default=timezone.now)

    @property
    def points():
        return 25
        

class Idea(Submission):
    title = models.CharField(max_length=200)
    description= models.TextField()
    submit_date = models.DateField(default=timezone.now)

    @property
    def points():
        return 50

    def __str__(self):
        return self.title



class Media(Submission):
    shared_post = models.ForeignKey("dashboard.ShareablePost",on_delete=models.CASCADE,related_name="media_submissions")
    submit_date = models.DateField(default=timezone.now)
    
    @property
    def points():
        return 50

    

