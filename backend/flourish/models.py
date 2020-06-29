from django.db import models


# user list
class Teacher(models.Model):
    user_id = models.CharField(
        max_length=100
    )
    name = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    real_name = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    phone = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    head_img = models.URLField(
        null=True,
        blank=True
    )
    create_time = models.DateTimeField(
        null=True,
        blank=True
    )
    is_active = models.BooleanField()
    has_course = models.BooleanField()
    is_reapply = models.BooleanField()
    is_fake = models.BooleanField()

    def __str__(self):
        return '{0}({1})'.format(
            self.real_name,
            self.phone
        )


# user info form
class InfoForm(models.Model):
    field_id = models.CharField(
        max_length=100
    )
    field_name = models.TextField(
        null=True,
        blank=True
    )
    field_value = models.TextField(
        null=True,
        blank=True
    )
    create_time = models.DateTimeField(
        null=True,
        blank=True
    )
    user_id = models.CharField(
        max_length=100
    )
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        related_name='infoForms'
    )

    def __str__(self):
        return '{1}({0})'.format(
            self.field_name,
            self.field_value
        )

# user course
class UserCourse(models.Model):
    user_course_id = models.CharField(
        max_length=100
    )
    user_id = models.CharField(
        max_length=100
    )
    tag_name = models.CharField(
        max_length=100
    )
    course_num = models.IntegerField()
    term_num = models.CharField(
        max_length=100
    )
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        related_name='userCourses'
    )

    def __str__(self):
        return '{0} | {1} | 学期：{2}'.format(
            self.teacher,
            self.tag_name,
            self.term_num
        )


# user protocal
class ApplyCourse(models.Model):
    stu_num = models.IntegerField(
        null=True,
        blank=True
    )
    teacher_num = models.IntegerField(
        null=True,
        blank=True
    )
    front_img = models.URLField(
        null=True,
        blank=True
    )
    back_img = models.URLField(
        null=True,
        blank=True
    )
    school_name = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    school_address = models.CharField(
        max_length=200,
        null=True,
        blank=True
    )
    _user_course_id = models.CharField(
        max_length=100
    )
    user_id = models.CharField(
        max_length=100
    )
    user_course = models.OneToOneField(
        UserCourse,
        on_delete=models.CASCADE
    )
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        related_name='applyCourses'
    )

    def __str__(self):
        return '{0} | {1}'.format(
            self.teacher,
            self.user_course
        )

# class form info
class FeedbackForm(models.Model):
    feedback_id = models.CharField(
        max_length=100
    )
    create_time = models.DateTimeField(
        null=True,
        blank=True
    )
    class_num = models.CharField(
        max_length=100
    )
    _user_course_id = models.CharField(
        max_length=100
    )
    user_id = models.CharField(
        max_length=100
    )
    user_course = models.ForeignKey(
        UserCourse,
        on_delete=models.CASCADE,
        related_name='feedback_forms'
    )
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.feedback_id



class FeedbackUnit(models.Model):
    field_id = models.CharField(
        max_length=100
    )
    field_name = models.TextField(
        null=True,
        blank=True
    )
    field_value = models.TextField(
        null=True,
        blank=True
    )
    feedback_id = models.CharField(
        max_length=100
    )
    _user_course_id = models.CharField(
        max_length=100
    )
    user_id = models.CharField(
        max_length=100
    )
    feedback_form = models.ForeignKey(
        FeedbackForm,
        on_delete=models.CASCADE,
        related_name='feedback_units'
    )
    user_course = models.ForeignKey(
        UserCourse,
        on_delete=models.CASCADE
    )
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return '{0}: {1}'.format(
            self.field_name,
            self.field_value
        )


class FeedbackPic(models.Model):
    pic_url = models.URLField(
        null=True,
        blank=True
    )
    feedback_id = models.CharField(
        max_length=100
    )
    _user_course_id = models.CharField(
        max_length=100
    )
    user_id = models.CharField(
        max_length=100
    )
    feedback_form = models.ForeignKey(
        FeedbackForm,
        on_delete=models.CASCADE,
        related_name='feedback_pics'
    )
    user_course = models.ForeignKey(
        UserCourse,
        on_delete=models.CASCADE,
        related_name='feedback_pics'
    )
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE
    )
