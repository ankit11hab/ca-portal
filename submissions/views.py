from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from .models import POC,Idea,Media,Submission
from .forms import POCForm,IdeaForm
from django.contrib import messages
import csv,io
# Create your views here.
from django import forms



class IdeaCreateView(CreateView):
    model=Idea
    form_class = IdeaForm

    def form_valid(self, form):
        form.instance.user = self.request.user
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
    return render(request,'submissions/home.html')

@login_required(login_url='login')
def tasks(request):
    return render(request,'submissions/tasks.html')

@login_required(login_url='login')
def ideas(request):
    userNow = request.user
    context = {
        'ideas': userNow.idea_subissions.all()
    }
    return render(request,'submissions/ideas.html',context)

@login_required(login_url='login')
def pocs(request):
    userNow = request.user
    context = {
        'pocs': userNow.poc_submissions.all()
    }
    return render(request,'submissions/pocs.html',context)
