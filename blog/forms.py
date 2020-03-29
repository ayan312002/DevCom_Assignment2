from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from blog.models import Article


class CustomSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, label='First Name')
    last_name = forms.CharField(max_length=30, required=False, label='Last Name')
    email = forms.EmailField(max_length=254, label='Email', help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['article_title', 'article_content']