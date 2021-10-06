from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from .models import POC,Idea,Media,Submission
from django.http import JsonResponse
import json
from .forms import POCForm,IdeaForm,MediaForm
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

class MediaCreateView(CreateView):
    model=Media
    form_class = MediaForm
    
    def get_form(self):
        data = json.loads(self.request.body)
        return MediaForm({
            "shared_post":data.get("shared_post")
        })
    def form_invalid(self, form):
        response = super(MediaCreateView,self).form_invalid(form)
        print(form)
        print(self.request.POST)
        return JsonResponse({
            "success":False,
            "error":form.errors
        }, status=400)

    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super(MediaCreateView, self).form_valid(form)
        data = {
            "success":True,
            'message': "Successfully submitted form data."
        }
        return JsonResponse(data)
    
        
    
@login_required(login_url='login')
def home(request):
    return render(request,'submissions/home.html',{'heading':'Submissions'})

@login_required(login_url='login')
def tasks(request):
    return render(request,'submissions/tasks.html',{'heading':'Tasks'})

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
