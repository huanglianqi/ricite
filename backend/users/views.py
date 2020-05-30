from django.contrib.auth.forms import User

from .serializers import UserSerializer
from rest_framework.generics import (
    GenericAPIView,
)
from rest_framework.mixins import (
    RetrieveModelMixin,
    UpdateModelMixin
)
from rest_framework.permissions import (
    IsAuthenticated,
)


class UserRetrieveUpdateAPIView(
    GenericAPIView,
    RetrieveModelMixin,
    UpdateModelMixin
):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        IsAuthenticated,
    ]
    lookup_field = 'username'

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
