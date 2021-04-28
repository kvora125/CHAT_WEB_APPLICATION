"""chat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url, include
from chatapp import views
from chatapp.views import index


urlpatterns = [
    url(r'^view_users/$', views.view_users),
    url(r'^save_msg/$', views.save_msg),
    url(r'^get_chat/$', views.get_chat),
    url(r'^view_msg/$', views.view_msg),
    url(r'^', index, name='index'),
]