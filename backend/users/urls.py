from django.urls import path, include

from .views import (
    UserRetrieveUpdateAPIView,
    UserPasswordResetAPIView,
    SubscribeEmailRetrieveUpdateAPIView,
)

urlpatterns = [
    path(
        'account/<str:username>/',
        UserRetrieveUpdateAPIView.as_view()
    ),
    path(
        'subscribeEmail/<str:name>/',
        SubscribeEmailRetrieveUpdateAPIView.as_view()
    ),
]
