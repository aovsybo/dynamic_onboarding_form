from django.urls import path

from .views import index, save_establishment


urlpatterns = [
    path('', index, name='index'),
    path('save/', save_establishment, name='save_establishment'),
]
