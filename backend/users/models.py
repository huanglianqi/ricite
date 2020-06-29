from django.db import models
from django.contrib.auth.models import User


class SubscribeEmail(models.Model):
    name = models.CharField(
        max_length=100
    )
    subscriber = models.ManyToManyField(
        User,
        related_name="subscribeEmails"
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return '{0} - {1}'.format(
            self.name,
            self.id
        )
