# Generated by Django 3.0.6 on 2020-06-09 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flourish', '0002_auto_20200609_1145'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='is_fake',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]