from django.db import models
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.



class Submission(models.Model):
    is_verified= models.BooleanField(default=False)
    user = models.ForeignKey(User,related_name="%(class)s_submissions",on_delete=models.CASCADE)
    submit_date = models.DateField(default=timezone.now)

    def get_absolute_url(self):
        return reverse("submissionhome")
    
    class Meta:
        abstract=True

class POC(Submission):
    name = models.CharField(max_length=70)
    design = models.CharField(max_length=60)
    college = models.CharField(max_length=90)
    contact = models.CharField(max_length=13)

    @property
    def points(self):
        if self.is_verified:
            return 25
        else:
            return 0
        

class Idea(Submission):
    title = models.CharField(max_length=200)
    description= models.TextField()

    @property
    def points(self):
        if self.is_verified:
            return 50
        else:
            return 0



class Media(Submission):
    shared_post = models.ForeignKey("dashboard.ShareablePost",on_delete=models.CASCADE,related_name="media_submissions")
    @property
    def points(self):
        return 50

    class Meta:
        unique_together = ('user','shared_post')
    

    
@receiver(post_save,sender=Media)
def update_points(sender,instance,*args,**kwargs):
    if instance.shared_post.is_facebook:
        instance.user.points+=instance.points 
        print(instance.points)
        instance.user.save()

@receiver(post_save,sender=Idea)
def update_points(sender,instance,*args,**kwargs):
    if instance.title:
        instance.user.points+=(instance.points) 
        print(instance)
        print(instance.points)
        instance.user.save()


@receiver(post_save,sender=POC)
def update_points(sender,instance,*args,**kwargs):
    if instance.name:
        instance.user.points+=(instance.points) 
        print(instance)
        print(instance.points)
        instance.user.save()

