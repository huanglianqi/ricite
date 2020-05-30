from django.urls import path

from .views import UserRetrieveUpdateAPIView

urlpatterns = [
    path(
        '<str:username>/',
        UserRetrieveUpdateAPIView.as_view()
    ),
]
