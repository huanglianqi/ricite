from django.urls import path, include

from .views import (
    UserRetrieveUpdateAPIView,
    UserPasswordResetAPIView
)

urlpatterns = [
    path(
        '<str:username>/',
        UserRetrieveUpdateAPIView.as_view()
    )
]
