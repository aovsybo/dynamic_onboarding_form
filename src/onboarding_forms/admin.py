from django.contrib import admin

from .models import EstablishmentType, Establishment, EstablishmentQuestion


admin.site.register(EstablishmentType)
admin.site.register(EstablishmentQuestion)
admin.site.register(Establishment)
