"""stocks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

# importing the views from view.py
from analysis.views import index, lists, post_detail, top, about

urlpatterns = [
    # Admin url
    url(r'^admin/', admin.site.urls),
    # Application URL
    url(r'^$',  index, name='index'),
    url(r'^lists/',  lists, name='lists'),
    url(r'^about/',  about, name='about'),
    url(r'^top/',  top, name='top'),
    url(r'^post/(?P<pk>[\w\-]+)/$', post_detail, name='post_detail'),
    
]
