# Generated by Django 3.0.6 on 2020-07-31 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flourish', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='share',
            name='user_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='share',
            name='user_real_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
