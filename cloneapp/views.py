from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm, NewsLetterForm, CommentsForm, UserPostForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Post, HashTag, Location, UserProfile
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, FormView,UpdateView

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
        # form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # login(request, user)
            user= form.cleaned_data.get('username')
            messages.success(request, f"Registration successfull {user}")
            return redirect('emaillogin')
        else:
            messages.error(request, "Unsuccessful registration. Invalid Information")
            return render(request, "registration/registration_form.html", {"signup_form":form})
    else:
        form = SignUpForm()
        return render(request, "registration/registration_form.html",{"signup_form":form})

def userlogin(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('index')
            else:
                messages.error(request, "Invalid username or password")
                return render(request, 'registration/registration_form.html')

        else:
            messages.error(request, "Invalid username or password")
    form = AuthenticationForm()
    return render(request, "registration/login.html",{"emaillogin_form":form})

def userlogout(request):
    logout(request)
    return HttpResponseRedirect('/landingpage/')

@login_required(login_url='/accounts/emaillogin/')
def  userhome(request):
    posts = Post.show_posts().order_by('-pub_date')
    return render(request, 'index.html', {"posts":posts})


@login_required(login_url='/account/login/')
def new_post(request):
    posts = Post.show_posts()

    if request.method == 'POST':
       post=request.FILES.get('image') 
       data=request.POST
       post=Post.objects.create(image=data['image'], author=data['author'], postcaption=data['postcaption'], location=data['location'], hashtag=data['hashtag'], pub_date=data['pub_date'])
       return redirect('landingpage')

    return render(request, 'index.html', context={'posts':posts})

def profilepage(request):
    current_user=request.user
    posts = Post.show_posts()

    return render(request, "profilepage.html",{"posts":posts})

@login_required(login_url='/account/login/')
def newpost(request):
    current_user=request.user
    userprofile = UserProfile.objects.get(username=current_user)

    if request.method == 'POST':
        form=UserPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.username = current_user
            post.save()

        return redirect('index')
    else:
        form=UserPostForm()
    return render(request, 'index.html', {"form": form})


# class SignupView(FormView):
#     template_name = 'registration_form'
#     form = SignUpForm
#     loginback = reverse_lazy('users:login')
#     def validate(self, form):
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.save()
#             return redirect('emaillogin')


# return HttpResponseRedirect(reverse('reviews:wine_detail', args=(wine.id,)))


class FindPostView(DetailView):
    model = Post
    template_name = 'findpost.html'