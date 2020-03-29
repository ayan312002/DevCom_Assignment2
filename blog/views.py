from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm

from blog.forms import CustomSignUpForm, ArticleForm
from blog.models import Article


def home_page(request):
    context = {

    }
    return render(request, 'blog/home.html',
                  context={"art": Article.objects.all})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/website/profile/')
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request,
                  template_name="blog/login.html",
                  context={"form": form})


def logout_request(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect("blog:home")


def register(request):
    if request.method == "POST":
        form = CustomSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            messages.success(request, f"Hi, {username}")
            return redirect("blog:home")
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

                return render(request, "blog/register.html", context={"form": form})

    form = CustomSignUpForm
    return render(request, "blog/register.html", context={"form": form})


def user_profile(request, article_id):
    user = request.user
    articles = Article.objects.filter(article_author= user)
    messages.error(request, "Work In Progress!")

    return render(request, 'blog/profile.html', context={"articles": articles})


@login_required(login_url='/login')
def article_new(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.article_author = request.user
            article.save()
            return redirect("blog:home")

    else:
        form = ArticleForm()
    return render(request, 'blog/add_article.html', context={"form": form})


def article_page(request, article_id):
    if not request.user.is_authenticated:
        messages.error(request, 'You need to be Logged in!')
        return redirect("blog:home")

    return render(request, 'blog/article.html',
                  context={"article": Article.objects.get(pk=article_id)})
