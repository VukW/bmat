from .models import Metadata
from rest_framework import serializers


class MetadataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metadata
        # fields = ['ISWC', 'title', 'contributors']
        fields = '__all__'