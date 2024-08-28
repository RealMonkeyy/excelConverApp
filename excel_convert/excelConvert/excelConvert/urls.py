from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('excelapp/', include('excelapp.urls')),
    path('', lambda request: redirect('format_conversion', permanent=False)),
]