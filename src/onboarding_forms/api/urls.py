from django.urls import path

from .views import home, questions, success


urlpatterns = [
    path('', home, name='home'),
    path('questions/<int:establishment_id>/', questions, name='questions'),
    path('success/', success, name='success'),
]