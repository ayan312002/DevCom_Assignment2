from django.conf.urls import url
from django.urls import path, include

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home_page, name='home'),
    path("register/", views.register, name="register"),
    path("logout/", views.logout_request, name="logout"),
    path("login/", views.login_request, name="login"),
    path('<int:article_id>', views.article_page, name="article"),
    # path('user/<str:author>', views.user_profile, name="user"),
    path('user/<int:article_id>', views.user_profile, name="user"),
    path('new', views.article_new, name='article_new')
]
