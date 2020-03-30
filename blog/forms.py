from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import Textarea

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
        article_content = forms.TimeField(widget=forms.Textarea(attrs={'size':'20',
                                                                       'style':'resize:none;'}))
        widgets = {'article_content': forms.Textarea(attrs={'rows': 6,
                                                            'size': '20',
                                                   'cols': 22,
                                                   'style': 'margin: 0px; height: 500px; width: 1280px;'}),
                   }
        fields = ['article_title', 'article_content']