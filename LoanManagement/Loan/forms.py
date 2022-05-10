from django.core import validators
from django import forms
from .models import Profile

class Registration(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['id','name','aadhar','pancard','salary','photo','bank','ctc','loan']