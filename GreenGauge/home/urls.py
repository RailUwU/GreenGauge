from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_dashboard, name='home_dashboard'),  # Root URL
    path('dashboard/', views.home_dashboard, name='home_dashboard'),  # Dashboard URL
    
]
