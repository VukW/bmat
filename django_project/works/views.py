from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse
from .models import Metadata
from rest_framework import viewsets
from .serializers import MetadataSerializer


def index(request):
    some_works = Metadata.objects.order_by('id')[:5]
    return JsonResponse(some_works)


def work(request, ISWC):
    work = Metadata.objects.get(ISWC=ISWC)
    serializer = MetadataSerializer(work)
    return JsonResponse(serializer.data)


class MetadataViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Metadata.objects.all().order_by('id')
    serializer_class = MetadataSerializer

# class MetadataView(views.):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = Metadata.objects.all().order_by('id')
#     serializer_class = MetadataSerializer