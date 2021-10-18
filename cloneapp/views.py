from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login
from .forms import SignUpForm

def landing(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
            messages.success(request, "Registration successfull")
            return redirect("cloneapp:index.html")
        messages.error(request, "Unsuccessful registration. Invalid Information")
    form = SignUpForm()
    return render(request=request, template_name="registration/emailsignup.html", context={"signup_form":form})
