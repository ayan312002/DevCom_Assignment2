from django import forms
from django.contrib.auth.models import User
from django.db import models
from datetime import datetime


class Article(models.Model):
    article_title = models.CharField(max_length=200)
    article_content = models.TextField()
    pub_date = models.DateTimeField('date published', default=datetime.now)
    article_author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.article_title
