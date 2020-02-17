from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url, include

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('<int:text_id>/home', views.homePost, name='homePost'),
    url(r'^login/$', auth_views.LoginView, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^settings/$', views.settings, name='settings'),
    # url(r'^settings/password/$', views.password, name='password'),
]
