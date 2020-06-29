# Generated by Django 3.0.6 on 2020-06-10 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flourish', '0006_auto_20200610_1442'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applycourse',
            name='font_img',
        ),
        migrations.AddField(
            model_name='applycourse',
            name='front_img',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='applycourse',
            name='back_img',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='applycourse',
            name='school_address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='applycourse',
            name='school_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='applycourse',
            name='stu_num',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='applycourse',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flourish.Teacher'),
        ),
        migrations.AlterField(
            model_name='applycourse',
            name='teacher_num',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='feedbackform',
            name='create_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='feedbackform',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flourish.Teacher'),
        ),
        migrations.AlterField(
            model_name='feedbackpic',
            name='pic_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='feedbackpic',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flourish.Teacher'),
        ),
        migrations.AlterField(
            model_name='feedbackunit',
            name='field_name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='feedbackunit',
            name='field_value',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='feedbackunit',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flourish.Teacher'),
        ),
        migrations.AlterField(
            model_name='infoform',
            name='create_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='infoform',
            name='field_name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='infoform',
            name='field_value',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='infoform',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flourish.Teacher'),
        ),
        migrations.AlterField(
            model_name='usercourse',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flourish.Teacher'),
        ),
    ]
