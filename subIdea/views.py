from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from .models import Post, Tasks, POC
from .forms import POCForm,PostForm
from django.contrib import messages
import csv,io
# Create your views here.
from django import forms



class PostCreateView(CreateView):
    model=Post
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.warning(self.request, f'Your idea has been submitted! Verification - Pending')
        return super().form_valid(form)

class POCCreateView(CreateView):
    model=POC
    form_class = POCForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.warning(self.request, f'Your POC has been submitted! Verification - Pending')
        return super().form_valid(form)
    

@login_required(login_url='login')
def home(request):
    userNow = request.user
    
    t = userNow.tasks_set.first()
    if userNow.post_set.first():
        t.ideaDone = userNow.post_set.first().validate
        t.save()

    t.points = 25*(int(t.ideaDone==1)+int(t.pocDone==1)+int(t.socialDone==1))
    t.save()
    contextTasks = {
        'tasks': userNow.tasks_set.all()
    }
    return render(request,'subIdea/home.html', contextTasks)


@login_required(login_url='login')
def ideas(request):
    userNow = request.user
    context = {
        'posts': userNow.post_set.all()
    }
    return render(request,'subIdea/ideas.html',context)

@login_required(login_url='login')
def pocs(request):
    userNow = request.user
    context = {
        'pocs': userNow.post_set.all()
    }
    return render(request,'subIdea/pocs.html',context)

@login_required(login_url='login')
def tasks(request):
    return render(request,'subIdea/tasks.html')
