from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import HttpResponse, redirect
from .forms import SignupForm, LoginForm, UploadFileForm
from .models import FoodImage
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from inference_sdk import InferenceHTTPClient
import google.generativeai as genai
from django.core.files.storage import FileSystemStorage
import base64
import re
from .utils import image_formatter
from PIL import Image

@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def gallery(request):
    images = FoodImage.objects.all()
    context = {
        'images': images,
    }
    return render(request, 'gallery.html', context)

def loginPage(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                messages.success(request, "Logged in succesfully!")
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Incorrect username or password!")
                return redirect('login')

        else:
            for error in form.errors.values():
                messages.error(request, error)
    else:
        form = LoginForm()
    return render(request, 'login.html', { 'form': form })


def registerPage(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful! Please log in")
            return redirect('login')
        else:
            for error in form.errors.values():
                messages.error(request, error)
    else:
        form = SignupForm()
    return render(request, 'register.html', { 'form': form })

def logoutPage(request):
    logout(request)
    return redirect('login')


def image_upload_view(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            img = form.save()
            # Open the image using PIL
            try:
                img = Image.open(img.image.path)
            except IOError:
                return HttpResponse("Image not found or cannot be opened.", status=404)
            # Process the image with Vishak's function
            processed_image = image_formatter(img)
            print(processed_image)
            return redirect('image_upload')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

        
