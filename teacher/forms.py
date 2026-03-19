from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Teacher
from scholarship.models import Scholarship

# ------------------ TEACHER REGISTRATION FORM ------------------
class TeacherRegistrationForm(UserCreationForm):
    class Meta:
        model = Teacher
        fields = ['email', 'password1', 'password2', 'name', 'qualification', 'phone', 'gender', 'address']

# ------------------ TEACHER LOGIN FORM ------------------
class TeacherLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

# ------------------ SCHOLARSHIP FORM ------------------
class ScholarshipForm(forms.ModelForm):
    class Meta:
        model = Scholarship
        fields = ['title', 'description', 'min_grade', 'max_grade', 'deadline']