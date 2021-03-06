# Generated by Django 3.0.6 on 2020-07-30 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeedbackForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback_id', models.CharField(max_length=100)),
                ('create_time', models.DateTimeField(blank=True, null=True)),
                ('class_num', models.CharField(max_length=100)),
                ('_user_course_id', models.CharField(max_length=100)),
                ('user_id', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Share',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.BooleanField(default=False)),
                ('user_id', models.CharField(max_length=100)),
                ('moment_id', models.CharField(max_length=100)),
                ('content', models.TextField(blank=True, null=True)),
                ('create_time', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=100)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('real_name', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=100, null=True)),
                ('head_img', models.URLField(blank=True, null=True)),
                ('create_time', models.DateTimeField(blank=True, null=True)),
                ('is_active', models.BooleanField()),
                ('has_course', models.BooleanField()),
                ('is_reapply', models.BooleanField()),
                ('is_fake', models.BooleanField()),
            ],
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
                ('is_fake', models.BooleanField(default=False)),
                ('has_protocal', models.BooleanField(default=False)),
                ('feedback_num', models.IntegerField()),
                ('finish_final', models.BooleanField()),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userCourses', to='flourish.Teacher')),
            ],
        ),
        migrations.CreateModel(
            name='SharePic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(blank=True, null=True)),
                ('like', models.BooleanField(default=False)),
                ('belongTo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sharePics', to='flourish.Share')),
            ],
        ),
        migrations.CreateModel(
            name='ShareLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=100)),
                ('user_name', models.CharField(max_length=100)),
                ('user_real_name', models.CharField(max_length=100)),
                ('share', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shareLikes', to='flourish.Share')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flourish.Teacher')),
            ],
        ),
        migrations.CreateModel(
            name='ShareComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('user_id', models.CharField(blank=True, max_length=100, null=True)),
                ('user_name', models.CharField(blank=True, max_length=100, null=True)),
                ('user_real_name', models.CharField(blank=True, max_length=100, null=True)),
                ('share', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shareCommnets', to='flourish.Share')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flourish.Teacher')),
            ],
        ),
        migrations.AddField(
            model_name='share',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flourish.Teacher'),
        ),
        migrations.CreateModel(
            name='InfoForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_id', models.CharField(max_length=100)),
                ('field_name', models.TextField(blank=True, null=True)),
                ('field_value', models.TextField(blank=True, null=True)),
                ('create_time', models.DateTimeField(blank=True, null=True)),
                ('user_id', models.CharField(max_length=100)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='infoForms', to='flourish.Teacher')),
            ],
        ),
        migrations.CreateModel(
            name='FeedbackUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_id', models.CharField(max_length=100)),
                ('field_name', models.TextField(blank=True, null=True)),
                ('field_value', models.TextField(blank=True, null=True)),
                ('feedback_id', models.CharField(max_length=100)),
                ('_user_course_id', models.CharField(max_length=100)),
                ('user_id', models.CharField(max_length=100)),
                ('create_time', models.DateTimeField(blank=True, null=True)),
                ('feedback_form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedback_units', to='flourish.FeedbackForm')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flourish.Teacher')),
                ('user_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flourish.UserCourse')),
            ],
        ),
        migrations.CreateModel(
            name='FeedbackPic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic_url', models.URLField(blank=True, null=True)),
                ('feedback_id', models.CharField(max_length=100)),
                ('_user_course_id', models.CharField(max_length=100)),
                ('user_id', models.CharField(max_length=100)),
                ('like', models.BooleanField(default=False)),
                ('create_time', models.DateTimeField(blank=True, null=True)),
                ('feedback_form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedback_pics', to='flourish.FeedbackForm')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flourish.Teacher')),
                ('user_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedback_pics', to='flourish.UserCourse')),
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
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedback_forms', to='flourish.UserCourse'),
        ),
        migrations.CreateModel(
            name='ApplyCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_num', models.IntegerField(blank=True, null=True)),
                ('teacher_num', models.IntegerField(blank=True, null=True)),
                ('front_img', models.URLField(blank=True, null=True)),
                ('back_img', models.URLField(blank=True, null=True)),
                ('school_name', models.CharField(blank=True, max_length=100, null=True)),
                ('school_address', models.CharField(blank=True, max_length=200, null=True)),
                ('_user_course_id', models.CharField(max_length=100)),
                ('user_id', models.CharField(max_length=100)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applyCourses', to='flourish.Teacher')),
                ('user_course', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='applycourse', to='flourish.UserCourse')),
            ],
        ),
    ]
