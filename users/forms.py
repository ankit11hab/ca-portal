from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import UserGroup, NewUser
from django.contrib.auth import get_user_model
from phonenumber_field.formfields import PhoneNumberField
User = get_user_model()


class SingleUserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'input_field', 'placeholder': 'Email'}))
    firstname = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input_field', 'placeholder': 'Full Name'}))
    referred_by = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input_field', 'placeholder': 'Enter referral id'}))
    phone = PhoneNumberField(widget=forms.TextInput(attrs={
                             'class': 'input_field', 'placeholder': 'Phone Number (e.g. +12125552368)'}), label="Phone number (e.g. +12125552368)", )

    graduation_year = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input_field', 'placeholder': 'graduation_year'}))
    college_city = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input_field', 'placeholder': 'college_city'}))
    college_state = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input_field', 'placeholder': 'college_state'}))
    college_name = forms.CharField(
        label="Full Name", widget=forms.TextInput(attrs={'class': 'input_field', 'placeholder': 'college_name'}))

    position_of_responsibility = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input_field', 'placeholder': 'position_of_responsibility'}))
    interested_modules = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input_field', 'placeholder': 'interested_modules'}))

    password1 = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input_field', 'placeholder': 'Password'}))
    password2 = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input_field', 'placeholder': 'Password confirm'}))

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
