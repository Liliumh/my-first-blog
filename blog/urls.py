from django.contrib.auth import views
from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]

# url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
# url(r'^accounts/login/$', views.login, name='login')
