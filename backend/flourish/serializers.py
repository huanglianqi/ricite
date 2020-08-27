from .models import (
    Teacher,
    InfoForm,
    UserCourse,
    UserCourseRemarks,
    ApplyCourse,
    FeedbackForm,
    FeedbackUnit,
    FeedbackPic,
    ShareComment,
    ShareLike,
    Share,
    SharePic
)

from django.contrib.auth.models import User

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


class infoFormSerializerForPic(serializers.ModelSerializer):
    class Meta:
        model = InfoForm
        fields = [
            'field_value',
            'field_id',
            'field_name'
        ]

class TeacherSerializerForPic(serializers.ModelSerializer):
    infoForms = infoFormSerializerForPic(
        read_only=True,
        many=True
    )

    class Meta:
        model = Teacher
        fields = [
            'infoForms',
            'real_name',
            'phone',
            'head_img',
            'name',
            'is_reapply'
        ]


class UserCourseSerializerForPic(serializers.ModelSerializer):
    class Meta:
        model = UserCourse
        fields = [
            'tag_name'
        ]



class FeedbackFormSerializerForPic(serializers.ModelSerializer):
    class Meta:
        model = FeedbackForm
        fields = [
            'create_time'
        ]


class FeedbackPicCollectSerializer(serializers.ModelSerializer):
    feedback_form = FeedbackFormSerializerForPic(
        read_only=True
    )
    teacher = TeacherSerializerForPic(read_only=True)
    user_course = UserCourseSerializerForPic(read_only=True)

    class Meta:
        model = FeedbackPic
        fields = [
            'pic_url',
            'feedback_form',
            'teacher',
            'user_course',
            'id',
            'like'
        ]


# Count applycourse instance teacher num, student num and school name
class ApplyCourseSerializerCount(serializers.ModelSerializer):
    class Meta:
        model = ApplyCourse
        fields = [
            'teacher_num',
            'stu_num',
            'school_name'
        ]


class UserCourseSerializerApplyCount(serializers.ModelSerializer):
    applycourse = ApplyCourseSerializerCount(read_only=True)

    class Meta:
        model = UserCourse
        fields = [
            'applycourse',
            'term_num',
            'course_num'
        ]


class TeacherSerializerForShareLikeAndComment(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = [
            'head_img',
            'phone',
            'real_name',
            'name'
        ]


# ---User--- #

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name'
        ]


# ---Feedback--- #

class FeedbackFormKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackForm
        fields = [
            'id',
            'class_num'
        ]


class FeedbackUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackUnit
        fields = [
            'field_name',
            'field_value'
        ]


class FeedbackPicSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackPic
        fields = [
            'pic_url'
        ]


class FeedbackFormRetrieveSerializer(serializers.ModelSerializer):
    feedback_units = FeedbackUnitSerializer(
        many=True,
        read_only=True
    )
    feedback_pics = FeedbackPicSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = FeedbackForm
        fields = [
            'create_time',
            'feedback_pics',
            'feedback_units'
        ]


# ---Teacher & Information Form--- #

class InfoFormRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoForm
        fields = [
            'field_name',
            'field_value'
        ]


class TeacherInfoFormRetrieveSerializer(serializers.ModelSerializer):
    infoForms = InfoFormRetrieveSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Teacher
        fields = [
            'infoForms'
        ]


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


# ---User Course--- #

class UserCourseAllListSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer(read_only=True)
    feedback_forms = FeedbackFormKeySerializer(
        many=True,
        read_only=True
    )
    applycourse = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = UserCourse
        fields = '__all__'


class UserCourseUpdateItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCourse
        fields = [
            'id',
            'is_fake',
            'mail_back'
        ]


class UserCourseRemarksCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCourseRemarks
        fields = '__all__'


class UserCourseRemarksDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCourseRemarks
        fields = '__all__'


class UserCourseRemarksDetailSerializer(serializers.ModelSerializer):
    fromPerson = UserSerializer()
    class Meta:
        model = UserCourseRemarks
        fields = [
            'fromPerson',
            'create_time',
            'content'
        ]


class UserCourseRemarksRetrieveSerializer(serializers.ModelSerializer):
    user_course_remarks = UserCourseRemarksDetailSerializer(many=True)

    class Meta:
        model = UserCourse
        fields = [
            'user_course_remarks'
        ]


# ---Apply Course--- #

class ApplyCourseRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplyCourse
        fields = [
            'stu_num',
            'teacher_num',
            'front_img',
            'back_img',
            'school_name',
            'school_address'
        ]


# ---Share--- #

class SharePicSerializer(serializers.ModelSerializer):
    class Meta:
        model = SharePic
        fields = [
            'like',
            'url'
        ]


class ShareCommentSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializerForShareLikeAndComment(read_only=True)

    class Meta:
        model = ShareComment
        fields = [
            'content',
            'teacher',
            'user_id',
            'user_name',
            'user_real_name'
        ]


class ShareLikeSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializerForShareLikeAndComment(read_only=True)

    class Meta:
        model = ShareLike
        fields = [
            'teacher',
            'user_id',
            'user_name',
            'user_real_name'
        ]


class ShareSrializer(serializers.ModelSerializer):
    sharePics = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='url'
    )
    shareComments = ShareCommentSerializer(
        many=True,
        read_only=True
    )
    shareLikes = ShareLikeSerializer(
        many=True,
        read_only=True
    )
    teacher = TeacherSerializerForPic(
        read_only=True
    )

    class Meta:
        model = Share
        fields = [
            'id',
            'like',
            'user_id',
            'moment_id',
            'content',
            'create_time',
            'shareLikes',
            'shareComments',
            'sharePics',
            'teacher',
            'user_real_name',
            'user_name'
        ]


class ShareUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Share
        fields = [
            'like',
            'moment_id'
        ]