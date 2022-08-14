from typing import NewType
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile, UserGroup, NewUser
from django.contrib.auth import get_user_model
from phonenumber_field.formfields import PhoneNumberField
User = get_user_model()


class SingleUserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'input_field', 'placeholder': 'Email *'}))
    firstname = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input_field', 'placeholder': 'Full Name *'}))
    referred_by = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'input_field', 'placeholder': 'Enter referral id'}))
    phone = PhoneNumberField(widget=forms.TextInput(attrs={
                             'class': 'input_field', 'placeholder': 'Phone Number (e.g. +12125552368) *'}), label="Phone number (e.g. +12125552368)", )

    graduation_year = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input_field', 'placeholder': 'Graduation Year *'}))
    college_city = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input_field', 'placeholder': 'College City *'}))
    college_state = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input_field', 'placeholder': 'College State *'}))
    college_name = forms.CharField(
        label="Full Name", widget=forms.TextInput(attrs={'class': 'input_field', 'placeholder': 'College Name *'}))
    
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input_field', 'placeholder': 'Password *'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input_field', 'placeholder': 'Confirm your Password *'}))

    def clean(self):
        cleaned_data = super(SingleUserRegisterForm, self).clean()
        referred_by = cleaned_data.get("referred_by")
        if referred_by:
            user = NewUser.objects.filter(alcherid=referred_by)
            if not user:
                raise forms.ValidationError("Referral ID is invalid")
        return self.cleaned_data

    class Meta:
        model = User
        fields = ['firstname', 'email', 'phone', 'graduation_year', 'college_state', 'college_city',
                  'college_name', 'referred_by']


class GroupUserRegisterFormForSingle(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'input_field', 'placeholder': 'Email *'}))
    firstname = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input_field', 'placeholder': 'Full Name *'}))
    # referred_by = forms.CharField(required=False, widget=forms.TextInput(
    #     attrs={'class': 'input_field', 'placeholder': 'Enter referral id'}))
    phone = PhoneNumberField(widget=forms.TextInput(attrs={
                             'class': 'input_field', 'placeholder': 'Phone Number (e.g. +12125552368) *'}), label="Phone number (e.g. +12125552368)", )

    graduation_year = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input_field', 'placeholder': 'Graduation Year *'}))

    class Meta:
        model = User
        fields = ['firstname', 'email', 'phone', 'graduation_year']


# incomplete
class GroupUserRegisterForm(forms.ModelForm):
    college_city = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input_field', 'placeholder': 'College City *'}))
    college_state = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input_field', 'placeholder': 'College State *'}))
    college_name = forms.CharField(
        label="Full Name", widget=forms.TextInput(attrs={'class': 'input_field', 'placeholder': 'College Name *'}))
    referred_by = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'input_field', 'placeholder': 'Enter referral id'}))

    def clean(self):
        cleaned_data = super(GroupUserRegisterForm, self).clean()
        referred_by = cleaned_data.get("referred_by")
        if referred_by:
            user = NewUser.objects.filter(alcherid=referred_by)
            if not user:
                raise forms.ValidationError("Referral ID is invalid")
        return self.cleaned_data

    class Meta:
        model = UserGroup
        fields = ['college_state', 'college_city',
                  'college_name', 'referred_by']


class UserUpdateForm(forms.ModelForm):

    firstname = forms.CharField(label="Full Name")
    phone = PhoneNumberField(widget=forms.TextInput(
    ), label="Phone number (e.g. +12125552368)", required=True)
    img = forms.ImageField()
    position_of_responsibility=forms.CharField(required=True)
    interested_modules=forms.CharField(required=True)
    fb_handle = forms.CharField(required=True,
        label="Facebook Handle", widget=forms.TextInput(attrs={'class': 'input_field'}))
    instahandle = forms.CharField(required=True,
        label="Instagram Handle", widget=forms.TextInput(attrs={'class': 'input_field'}))

    class Meta:
        model = User
        fields = ['firstname', 'phone', 'graduation_year', 'college_state',
                  'college_city', 'college_name',  'position_of_responsibility', 'interested_modules', 'img','instahandle', 'fb_handle']
