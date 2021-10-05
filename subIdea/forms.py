from django.db.models import fields
from django.forms import ModelForm
from django.forms import Textarea
from .models import POC,Post
from django import forms


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["subject","tell_us_your_idea"]
        widgets = {
            'subject': Textarea(attrs={'cols':30, 'rows':1,'placeholder': 'Your Idea *'}),
            'tell_us_your_idea': Textarea(attrs={'cols':40, 'rows':10,'placeholder': 'Description *'}),
        }

class POCForm(ModelForm):
    class Meta:
        model = POC
        fields = ['name','design','college','contact']
        widgets = {
            'name': Textarea(attrs={'cols':30, 'rows':1,'placeholder': 'POC Name *'}),
            'design': Textarea(attrs={'cols':30, 'rows':1,'placeholder': 'POC Designation *'}),
            'college': Textarea(attrs={'cols':30, 'rows':1,'placeholder': 'POC College *'}),
            'contact': Textarea(attrs={'cols':30, 'rows':1,'placeholder': 'POC Contact *'}),
        }
        
      
