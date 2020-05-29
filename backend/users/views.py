from django.contrib.auth.forms import User
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import UserSerializer

from rest_framework import (
    viewsets,
    filters
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
    )
    search_fields = [
        'username'
    ]

    def perform_update(self, serializer):
        instance = serializer.save()

    def perform_create(self, serializer):
        pass
