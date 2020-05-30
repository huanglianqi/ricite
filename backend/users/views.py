from django.contrib.auth.forms import User

from .serializers import UserSerializer
from rest_framework.generics import (
    RetrieveUpdateAPIView
)
from rest_framework.permissions import (
    IsAuthenticated,
)


class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        IsAuthenticated,
    ]
    lookup_field = 'username'
