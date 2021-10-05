from django.db.models import fields
from django.forms import ModelForm
from django.forms import Textarea
from .models import POC,Idea
from django import forms


class IdeaForm(ModelForm):
    class Meta:
        model = Idea
        fields = ["title","description"]
        widgets = {
            'title': Textarea(attrs={'cols':30, 'rows':1,'placeholder': 'Your Idea *'}),
            'description': Textarea(attrs={'cols':40, 'rows':10,'placeholder': 'Tell us more about your idea*'}),
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
        
      
