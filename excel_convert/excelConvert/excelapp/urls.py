from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.format_conversion, name='format_conversion'),
    path('config/upload/', views.config_upload, name='config_upload'),
    path('config/list/', views.config_list, name='config_list'),
    path('config/edit/<int:pk>/', views.config_edit, name='config_edit'),
    path('config/delete/<int:pk>/', views.config_delete, name='config_delete'),
]