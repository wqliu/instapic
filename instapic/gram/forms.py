from django import forms
from .models import Profile, Image
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PostForm(forms.ModelForm):
  class Meta:
    model = Image
    fields = ('image_caption', 'image', 'tag_someone',)

class SignUpForm(UserCreationForm):
  class Meta:
    model = User
    fields = ('username','email','password1','password2')