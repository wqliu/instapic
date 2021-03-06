from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf.urls import url, include
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import login as auth_login
from .forms import PostForm
from django.conf.urls.static import static
from .models import Profile, Image
from django.contrib.auth.models import User
from . import models
from .forms import SignUpForm
from django.contrib.auth.forms import UserCreationForm
from rest_framework import viewsets
from gram.serializers import ProfileSerializer
from django.core.mail import send_mail

'''
send mail enables sends confirmation mail using @gmail
'''
from django.contrib.auth.decorators import login_required

'''
The @login_required declarator limits access of view function to only 
authenticated users
'''
# ---------------------------------------------------------------------#
'''End Of Import'''
# ---------------------------------------------------------------------#

# VIEW FUNCTIONS HERE!
@login_required(login_url='/accounts/login/')
def index(request):
    all_images = Image.objects.all()
    all_users = Profile.objects.all()
    next = request.GET.get('next')
    if next: return redirect(next)
    return render(request, 'display/home.html', {"all_images": all_images}, {"all_users": all_users})

@login_required(login_url='/accounts/login/')
def explore(request):
    return render(request, 'display/explore.html')

@login_required(login_url='/accounts/login/')
def notification(request):
    return render(request, 'display/notification.html')

@login_required(login_url='/accounts/login/')
def profile(request):
    return render(request, 'display/userprofile.html')

def logout(request):
    return render(request, 'registration/logout.html')

def login(request):
    return render(request, 'registration/login.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'registration/registration_form.html', {'form': form})

@login_required(login_url='/accounts/login/')
def upload(request):
    current_user = request.user
    p = Profile.objects.filter(id=current_user.id).first()
    imageuploader_profile = Image.objects.filter(imageuploader_profile=p).all()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.imageuploader_profile = p
            post.save()
            return redirect('/')
    else:
        form = PostForm
    return render(request, 'display/upload.html', {"form": form})

#################################################################################################################################################################################
# LIKE IMAGE VIEW FUNCTION
#################################################################################################################################################################################

# Like view function


#################################################################################################
# rest framework for Profile
#################################################################################################
class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Profile.objects.all()[:10]
    serializer_class = ProfileSerializer
