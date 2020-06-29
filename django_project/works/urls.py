from django.urls import path, include

from . import views
from rest_framework import routers, serializers, viewsets

router = routers.DefaultRouter()
router.register(r'all', views.MetadataViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('work/<ISWC>', views.work, name='work'),
    path('', include(router.urls)),
]
