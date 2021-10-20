from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from .models import Post, HashTag, Location

def landing(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
            messages.success(request, "Registration successfull")
            return redirect("cloneapp:index.html")
        messages.error(request, "Unsuccessful registration. Invalid Information")
    form = SignUpForm()
    return render(request, 'home.html', context={"signup_form":form})


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # login(request, user)
            messages.success(request, "Registration successfull")
            return redirect('emaillogin')
        else:
            messages.error(request, "Unsuccessful registration. Invalid Information")
    else:
        form = SignUpForm()
        return render(request, "registration/emailsignup.html",{"signup_form":form})

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return render(request, 'index.html')
            else:
                messages.error(request, "Invalid username or password")
                return render(request, 'registration/emailsignup.html')

        else:
            messages.error(request, "Invalid username or password")
    form = AuthenticationForm()
    return render(request, "registration/emaillogin.html",{"emaillogin_form":form})


@login_required(login_url='/accounts/emaillogin/')
def  userhome(request):
    posts = Post.show_posts()
    return render(request, 'index.html', {"posts":posts})

def new_post(request):
    posts = Post.show_posts()

    if request.method == 'POST':
       post=request.FILES.get('image') 
       data=request.POST
       post=Post.objects.create(image=data['image'], author=data['author'], postcaption=data['postcaption'], location=data['location'], hashtag=data['hashtag'], pub_date=data['pub_date'])
       return redirect('landingpage')

    return render(request, 'index.html', context={'posts':posts})