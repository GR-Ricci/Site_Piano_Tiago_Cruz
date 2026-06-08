from django.urls import path
from . import views

app_name = 'piano'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('classes/', views.classes, name='classes'),
    path('usp/', views.usp, name='usp'),
    path('video-instituto/', views.stream_video, name='video_instituto'),
]

