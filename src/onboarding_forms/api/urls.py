from django.urls import path

from .views import home, questions, success, establishments


urlpatterns = [
    path('', home, name='home'),
    path('questions/<int:establishment_id>/', questions, name='questions'),
    path('success/', success, name='success'),
    path('establishments/', establishments, name='establishments'),
]
