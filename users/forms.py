from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import UserGroup, NewUser
from django.contrib.auth import get_user_model
from phonenumber_field.formfields import PhoneNumberField
User = get_user_model()


class SingleUserRegisterForm(UserCreationForm):
    firstname = forms.CharField(label="Full Name")
    referred_by = forms.CharField(label="Enter referral id")
    phone = PhoneNumberField(widget=forms.TextInput(
    ), label="Phone number (e.g. +12125552368)", required=False)
    widgets = {
        'email': forms.EmailInput(attrs={'class': 'input_field', 'placeholder': 'Email'}),
    }
    class Meta:
        model = User
        fields = ['firstname', 'email', 'phone', 'graduation_year', 'college_state', 'college_city',
                  'college_name', 'position_of_responsibility', 'interested_modules', 'referred_by']

    


class GroupUserRegisterFormForSingle(forms.ModelForm):
    email = forms.EmailField(label="Email")
    firstname = forms.CharField(label="Full Name")
    phone = PhoneNumberField(widget=forms.TextInput(
    ), label="Phone number (e.g. +12125552368)", required=False)

    class Meta:
        model = User
        fields = ['firstname', 'email', 'phone', 'graduation_year',
                  'position_of_responsibility', 'interested_modules']


# incomplete
class GroupUserRegisterForm(forms.ModelForm):
    class Meta:
        model = UserGroup
        fields = ['college_state', 'college_city', 'college_name']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(label="Email")
    firstname = forms.CharField(label="Full Name")
    phone = PhoneNumberField(widget=forms.TextInput(
    ), label="Phone number (e.g. +12125552368)", required=False)

    class Meta:
        model = User
        fields = ['firstname', 'email', 'phone', 'graduation_year', 'college_state',
                  'college_city', 'college_name',  'position_of_responsibility', 'interested_modules']
