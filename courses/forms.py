from django import forms
from .models import Department, Course, Student

class ProfileChangeForm(forms.ModelForm):
    class Meta:
        model = Student 
        fields = ['grad_year', 'major', 'minor', 'interests']


