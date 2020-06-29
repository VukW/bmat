from .models import Metadata, Contributor
from rest_framework import serializers


class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = ['name']


class MetadataSerializer(serializers.HyperlinkedModelSerializer):
    contributors = ContributorSerializer(many=True, read_only=True)

    class Meta:
        model = Metadata
        fields = ['ISWC', 'title', 'contributors']
        # fields = '__all__'
        depth = 1
