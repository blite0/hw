"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from myapp.views import *

urlpatterns = [
    path('', include('myapp.urls')),
    path('', index, name='index'),
    path('article/', main_article, name='mail_article'),
    path('article/archive/', second_arhive, name='second_arhive'),
    path('users', users, name='users'),
    path('article/33/', uniq_article, name='uniq_article'),
    path('article/<int:article_id>/', article, name='article'),
    path('article/<int:article_id>/<slug:name>', article, name='article_name'),
    path('users/<int:user_number>', users_number, name='users_names'),
    re_path(r'\b050\d{7}\b|066\d{7}\b|099\d{7}\b|095\d{7}\b|'
            r'067\d{7}\b|068\d{7}\b|096\d{7}\b|097\d{7}\b|'
            r'098\d{7}\b|063\d{7}\b|073\d{7}\b|093\d{7}\b|089\d{7}\b|094\d{7}\b',
            mobile_number),
    re_path(r'\b[a-f0-9]{4}[-]{1}[a-f0-9]{6}\b', hw_five)
]
