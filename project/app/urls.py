from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='upload_video'),
]