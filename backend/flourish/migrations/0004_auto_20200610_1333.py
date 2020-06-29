# Generated by Django 3.0.6 on 2020-06-10 05:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flourish', '0003_teacher_is_fake'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedbackForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback_id', models.CharField(max_length=100)),
                ('create_time', models.DateTimeField()),
                ('class_num', models.CharField(max_length=100)),
                ('_user_course_id', models.CharField(max_length=100)),
                ('user_id', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='teacher',
            name='has_course',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='is_reapply',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='create_time',
            field=models.DateTimeField(),
        ),
        migrations.CreateModel(
            name='UserCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_course_id', models.CharField(max_length=100)),
                ('user_id', models.CharField(max_length=100)),
                ('tag_name', models.CharField(max_length=100)),
                ('course_num', models.IntegerField()),
                ('term_num', models.CharField(max_length=100)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flourish.Teacher')),
            ],
        ),
        migrations.CreateModel(
            name='InfoForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_id', models.CharField(max_length=100)),
                ('field_name', models.TextField()),
                ('field_value', models.TextField()),
                ('create_time', models.DateTimeField()),
                ('user_id', models.CharField(max_length=100)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flourish.Teacher')),
            ],
        ),
        migrations.CreateModel(
            name='FeedbackUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_id', models.CharField(max_length=100)),
                ('field_name', models.TextField()),
                ('field_value', models.TextField()),
                ('feedback_id', models.CharField(max_length=100)),
                ('_user_course_id', models.CharField(max_length=100)),
                ('user_id', models.CharField(max_length=100)),
                ('feedback_form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flourish.FeedbackForm')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flourish.Teacher')),
                ('user_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flourish.UserCourse')),
            ],
        ),
        migrations.CreateModel(
            name='FeedbackPic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic_url', models.URLField()),
                ('feedback_id', models.CharField(max_length=100)),
                ('_user_course_id', models.CharField(max_length=100)),
                ('user_id', models.CharField(max_length=100)),
                ('feedback_form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flourish.FeedbackForm')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flourish.Teacher')),
                ('user_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flourish.UserCourse')),
            ],
        ),
        migrations.AddField(
            model_name='feedbackform',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flourish.Teacher'),
        ),
        migrations.AddField(
            model_name='feedbackform',
            name='user_course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flourish.UserCourse'),
        ),
        migrations.CreateModel(
            name='ApplyCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_num', models.IntegerField()),
                ('teacher_num', models.IntegerField()),
                ('font_img', models.URLField()),
                ('back_img', models.URLField()),
                ('school_name', models.CharField(max_length=100)),
                ('school_address', models.CharField(max_length=200)),
                ('_user_course_id', models.CharField(max_length=100)),
                ('user_id', models.CharField(max_length=100)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flourish.Teacher')),
                ('user_course', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='flourish.UserCourse')),
            ],
        ),
    ]
