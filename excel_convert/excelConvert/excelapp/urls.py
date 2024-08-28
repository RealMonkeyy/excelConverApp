from django.urls import path
from . import views

urlpatterns = [
    path('config/', views.config_upload, name='config_upload'),
    path('convert/', views.format_conversion, name='format_conversion'),
]