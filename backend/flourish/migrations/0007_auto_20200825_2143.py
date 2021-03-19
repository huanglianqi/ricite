# Generated by Django 3.0.6 on 2020-08-25 13:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('flourish', '0006_auto_20200825_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercourseremarks',
            name='forUserCourse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_course_remarks', to='flourish.UserCourse'),
        ),
        migrations.AlterField(
            model_name='usercourseremarks',
            name='fromPerson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_course_remarks', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='usercourseremarks',
            name='toPerson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_course_remarks', to='flourish.Teacher'),
        ),
    ]