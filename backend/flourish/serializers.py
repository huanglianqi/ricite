from .models import (
    Teacher,
    InfoForm,
    UserCourse,
    ApplyCourse,
    FeedbackForm,
    FeedbackUnit,
    FeedbackPic,
)

from rest_framework import serializers


class TeacherSerializer(serializers.ModelSerializer):
    userCourses = serializers.StringRelatedField(
        many=True
    )
    applyCourses = serializers.StringRelatedField(
        many=True
    )
    infoForms = serializers.StringRelatedField(
        many=True
    )
    class Meta:
        model = Teacher
        fields = '__all__'


class InfoFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoForm
        fields = '__all__'


class UserCourseSerializer(serializers.ModelSerializer):
    feedback_forms = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='id'
    )
    class Meta:
        model = UserCourse
        fields = '__all__'


class ApplyCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplyCourse
        fields = '__all__'


class FeedbackFormSerializer(serializers.ModelSerializer):
    feedback_units = serializers.StringRelatedField(
        many=True
    )
    feedback_pics = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='pic_url'
    )
    class Meta:
        model = FeedbackForm
        fields = '__all__'


class FeedbackUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackUnit
        fields = '__all__'


class FeedbackPicSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackPic
        fields = '__all__'


# return data noly contains question and answer
class BaseInfoFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoForm
        fields = [
            'field_name',
            'field_value'
        ]


# return data contains
# full Teacher data and InfoForm which related to
class TeacherSerializerInfo(serializers.ModelSerializer):
    infoForms = BaseInfoFormSerializer(many=True,read_only=True)
    class Meta:
        model = Teacher
        fields = '__all__'


# return data contains
# full UserCourse data and TeacherInfo which related to
class UserCourseSerializerTeacherInfo(serializers.ModelSerializer):
    teacher = TeacherSerializerInfo(read_only=True)
    feedback_forms = FeedbackFormSerializer(
        many=True,
        read_only=True
    )
    class Meta:
        model = UserCourse
        fields = '__all__'


# return data contains
# full ApplyCourse data and TeacherInfo which related to
class ApplyCourseSerializerTeacherInfo(serializers.ModelSerializer):
    teacher = TeacherSerializerInfo(read_only=True)
    class Meta:
        model = ApplyCourse
        fields = '__all__'


class UserCourseSerializerFeedbackForm(serializers.ModelSerializer):
    feedback_forms = FeedbackFormSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = UserCourse
        fields = '__all__'


class TeacherSerializerUserCourse(serializers.ModelSerializer):
    userCourses = UserCourseSerializer(
        read_only=True,
        many=True
    )

    class Meta:
        model = Teacher
        fields = '__all__'
