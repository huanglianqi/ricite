from django.contrib.auth.forms import User

from .models import SubscribeEmail

from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import (
    reset_password_token_created,
    post_password_reset,
)

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from .serializers import (
    UserSerializer,
    SubscribeEmailSerializer
)

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


class UserRetrieveUpdateAPIView(
    GenericAPIView,
    RetrieveModelMixin,
    UpdateModelMixin
):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
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
            'reset_password_url': "https://admin.ricifoundation.com/#/resetPassword?token={}".format(reset_password_token.key),
            'title': '密码重置',
        }

        # render email text
        email_html_message = render_to_string('user_reset_password.html', context)
        # email_plaintext_message = render_to_string('user_reset_password.txt', context)

        msg = EmailMultiAlternatives(
            # title:
            "日慈信息管理平台 | 密码重置",
            # message:
            # email_plaintext_message,
            "Reset Password",
            # from:
            "huanglianqi@ricifoundation.com",
            # to:
            [reset_password_token.user.email]
        )
        msg.attach_alternative(email_html_message, "text/html")
        msg.send()

    @receiver(post_password_reset)
    def post_password_reset(sender, user, *args, **kwargs):
        """
          post notions about resetting password successfully
        """
        content = {
            'username': user.username,
            'lastname': user.last_name,
            'firstname': user.first_name,
            'email': user.email,
            'title': '密码重置成功',
        }

        email_html_message = render_to_string('user_reset_password_success.html', content)

        msg = EmailMultiAlternatives(
            '日慈信息管理平台 | 密码重置成功',
            'Reset Password Successfully',
            'admin@ricifoundation.com',
            [user.email]
        )
        msg.attach_alternative(email_html_message, "text/html")
        msg.send()


class SubscribeEmailRetrieveUpdateAPIView(
    GenericAPIView,
    RetrieveModelMixin,
    UpdateModelMixin
):
    queryset = SubscribeEmail.objects.all()
    serializer_class = SubscribeEmailSerializer
    permission_classes = [
        IsAuthenticated
    ]
    lookup_field = 'name'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
