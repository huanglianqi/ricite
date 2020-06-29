from django.contrib.auth.forms import User

from .models import SubscribeEmail

from rest_framework import serializers


class SubscribeEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscribeEmail
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    subscribeEmails = serializers.SlugRelatedField(
        many=True,
        queryset=SubscribeEmail.objects.all(),
        slug_field='name'
    )
    class Meta:
        model = User
        fields = '__all__'
