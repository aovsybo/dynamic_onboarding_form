from rest_framework import serializers

from ..models import EstablishmentType, Establishment


class EstablishmentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstablishmentType
        fields = '__all__'


class EstablishmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Establishment
        fields = '__all__'
