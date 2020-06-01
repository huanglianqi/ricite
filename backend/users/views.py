from django.contrib.auth.forms import User

from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

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

from django.contrib.auth import update_session_auth_hash

# from django.dispatch import receiver
# from django.core.mail import EmailMultiAlternatives

#from django_rest_passwordreset.signals import (
#    reset_password_token_created,
#)


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


class UserPasswordResetAPIView(GenericAPIView):
    @receiver(reset_password_token_created)
    def password_reset_token_created(sender, reset_password_token, *args, **kwargs):
        """
          Handles password reset tokens
          When a token is created, an e-mail needs to be sent to the user
        """
        # send an e-mail to the user
        context = {
            'current_user': reset_password_token.user,
            'username': reset_password_token.user.username,
            'email': reset_password_token.user.email,
            'firstname': reset_password_token.user.first_name,
            'lastname': reset_password_token.user.last_name,
            'reset_password_url': "http://localhost:8080/#/resetPassword?token={}".format(reset_password_token.key),
        }

        # render email text
        email_html_message = render_to_string('user_reset_password.html', context)
        # email_plaintext_message = render_to_string('user_reset_password.txt', context)

        msg = EmailMultiAlternatives(
            # title:
            "Password Reset",
            # message:
            # email_plaintext_message,
            "test",
            # from:
            "huanglianqi@ricifoundation.com",
            # to:
            [reset_password_token.user.email]
        )
        msg.attach_alternative(email_html_message, "text/html")
        msg.send()

