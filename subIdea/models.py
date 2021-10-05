from django.db import models
from django.urls import reverse
from django.db.models.signals import post_save
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.



class Submission(models.Model):
    class SubmissionType(models.TextChoice):
        IDEA="I",_("Idea")
        POC="P",_("Poc")
        MEDIA="M",_('Media')

    is_verified= models.BooleanField(default=False)
    submission_type = models.CharField(blank=True,null=True,choices=SubmissionType.choices)

    class Meta:
        abstract= True

class POC(Submission):
    user = models.ForeignKey(User,related_name="%(class)%_submissions",on_delete=models.CASCADE)
    name = models.CharField(max_length=70)
    design = models.CharField(max_length=60)
    college = models.CharField(max_length=90)
    contact = models.CharField(max_length=13)
    submit_date = models.DateField(default=timezone.now)

    @property
    def points():
        return 25
        



class Idea(Submission):
    user = models.ForeignKey(User,related_name="%(class)%_submissions",on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    idea = models.TextField()
    submit_date = models.DateField(default=timezone.now)

    @property
    def points():
        return 25

    def __str__(self):
        return self.title



class Media(Submission):
    user = models.ForeignKey(User,related_name="%(class)%_submissions",on_delete=models.CASCADE)
    shared_post = models.ForeignKey("dashboard.SharedPost",on_delete=models.CASCADE,related_name="media_submissions")
    submit_date = models.DateField(default=timezone.now)
    
    @property
    def points():
        return 25

    





def change_Points(sender,instance,created,**kwargs):
    t = instance
    if t.points != 25*(int(t.ideaDone==1)+int(t.pocDone==1)+int(t.socialDone==1)):
        t.points = 25*(int(t.ideaDone==1)+int(t.pocDone==1)+int(t.socialDone==1))
        t.save()
        print("Points updated")

def create_Tasks(sender,instance,created,**kwargs):
    if created:
        Tasks.objects.create(user=instance)
        print("Tasks created")

post_save.connect(create_Tasks, sender=User)
post_save.connect(change_Points, sender=Tasks)
