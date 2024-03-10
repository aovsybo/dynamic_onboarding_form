from django.contrib import admin

from .models import EstablishmentType, Establishment, EstablishmentQuestion, ClientResponse


admin.site.register(EstablishmentType)
admin.site.register(EstablishmentQuestion)
admin.site.register(Establishment)
admin.site.register(ClientResponse)
