from .models import (
    Teacher,
    InfoForm,
    UserCourse,
    ApplyCourse,
    FeedbackForm,
    FeedbackUnit,
    FeedbackPic,
)

from .serializers import (
    TeacherSerializer,
    InfoFormSerializer,
    UserCourseSerializer,
    ApplyCourseSerializer,
    FeedbackFormSerializer,
    FeedbackUnitSerializer,
    FeedbackPicSerializer,
    UserCourseSerializerTeacherInfo,
    ApplyCourseSerializerTeacherInfo,
    TeacherSerializerUserCourse,
    FeedbackPicCollectSerializer,
)

from rest_framework.generics import(
    GenericAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    ListAPIView,
)
from rest_framework.mixins import (
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny
)

from rest_framework import filters

from django_filters.rest_framework import DjangoFilterBackend

from django.db.models import Q

from datetime import datetime


class TeacherListAPIView(ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend
    ]
    filterset_fields = [
        'is_active',
        'has_course',
        'is_reapply',
        'is_fake'
    ]
    search_fields = [
        'name',
        'real_name',
        'phone'
    ]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class TeacherRetrieveUpdateAPIView(
    GenericAPIView,
    RetrieveModelMixin,
    UpdateModelMixin
):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_class = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    # use for modify is_fake
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class InfoFormListAPIView(ListAPIView):
    queryset = InfoForm.objects.all()
    serializer_class = InfoFormSerializer
    permission_classes = [AllowAny]
    filter_backends = [
        DjangoFilterBackend
    ]
    filterset_fields = ['user_id']

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class UserCourseListAPIView(ListAPIView):
    queryset = UserCourse.objects.order_by('-user_course_id')
    serializer_class = UserCourseSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        'user_id',
        'tag_name',
        'term_num'
    ]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ApplyCourseListAPIView(ListAPIView):
    queryset = ApplyCourse.objects.all()
    serializer_class = ApplyCourseSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user_id']

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class FeedbackFormRetrieveAPIView(RetrieveAPIView):
    queryset =FeedbackForm.objects.all()
    serializer_class = FeedbackFormSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class FeedbackFormListAPIView(ListAPIView):
    queryset = FeedbackForm.objects.all()
    serializer_class = FeedbackFormSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        '_user_course_id',
        'id',
        'class_num'
    ]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class FeedbackUnitRetrieveAPIView(RetrieveAPIView):
    queryset =FeedbackUnit.objects.all()
    serializer_class = FeedbackUnitSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class FeedbackUnitListAPIView(ListAPIView):
    queryset = FeedbackUnit.objects.all()
    serializer_class = FeedbackUnitSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        'user_id',
        'feedback_id',
        'id',
        'field_name'
    ]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class FeedbackPicAPIListView(ListAPIView):
    queryset = FeedbackPic.objects.all()
    serializer_class = FeedbackPicSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        'user_id',
        'feedback_id'
    ]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class FeedbackPicRetrieveAPIView(RetrieveAPIView):
    queryset = FeedbackPic.objects.all()
    serializer_class = FeedbackPicSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


# return instance which applycourse is not exist
def applycourseNotExist(instance):
    try:
        instance.applycourse
        return None
    except ApplyCourse.DoesNotExist:
        return instance


def applycourseExist(instance):
    try:
        instance.applycourse
        return instance
    except ApplyCourse.DoesNotExist:
        return None


# get the list of teachers
# who have course
# but not sign protocal
# in certain term
# Each item in list is UserCourseSerializer instance
class NoProtocalListAPIView(ListAPIView):
    serializer_class = UserCourseSerializerTeacherInfo
    permission_classes = [AllowAny]

    def get_queryset(self):
        term = self.kwargs['term']

        # item filter by term and applycourse exist
        # sign protocal will create one ApplyCourse instance related to item
        return list(
            filter(
                lambda item: applycourseNotExist(item),
                UserCourse.objects.filter(
                    term_num=term,
                    is_fake=False
                )
            )
        )

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


# get list of teacher
# who have not feedback for course
# in certain term
# Each item in list is UserCourseSerializer instance
class NoFeedbackListAPIView(ListAPIView):
    serializer_class = UserCourseSerializerTeacherInfo
    permission_classes = [AllowAny]

    def get_queryset(self):
        term = self.kwargs['term']

        # item filter by term and feedback form list is empty
        # have feedback will put certain FeedbackForm instance into feedback_forms list
        # sum feedback forms = course_num + ONE finish form !!!
        return list(
            filter(
                lambda item: item.feedback_forms.count() == 0,
                list(
                    filter(
                        lambda item: applycourseExist(item),
                        UserCourse.objects.filter(
                            term_num=term,
                            is_fake=False
                        )
                    )
                )
            )
        )

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


# get list of teachers
# who have feedback for course
# but not complete all feedback form
# in certain term
# Each item in list is UserCourseSerializer instance
class NoAllFeedbackListAPIView(ListAPIView):
    serializer_class = UserCourseSerializerTeacherInfo
    permission_classes = [AllowAny]

    def get_queryset(self):
        term = self.kwargs['term']

        # item filter by term and length of feedback form list less than course_num and more than 0
        # sum feedback forms = course_num + ONE finish form !!!
        return list(
            filter(
                lambda item: item.feedback_forms.count() < item.course_num + 1 and item.feedback_forms.count() > 0,
                UserCourse.objects.filter(
                    term_num=term,
                    is_fake=False
                )
            )
        )

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


# get list of teachers
# who have totally completed all feedback forms
# in certain term
# Each item in list is UserCourseSerializer instance
class IsAllFeedbackListAPIView(ListAPIView):
    serializer_class = UserCourseSerializerTeacherInfo
    permission_classes = [AllowAny]

    def get_queryset(self):
        term = self.kwargs['term']

        # item filter by term and length of feedback form list less than course_num
        # sum feedback forms = course_num + one finish forms
        # sum feedback forms = course_num + ONE finish form !!!
        return list(
            filter(
                lambda item: item.feedback_forms.count() == item.course_num + 1,
                UserCourse.objects.filter(
                    term_num=term,
                    is_fake=False
                )
            )
        )

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


# if course num less than or eq to 3, teachers must complete all feedback forms
# if course num less than or eq to 7 and more than 3, teachers can skip ONE feedback form for some reason
# if course num more than or eq to 8, can skip TWO
# if True, will return a item instance
def NoFinishCourse(item):
    feedback_num = item.feedback_forms.count()
    course_num = item.course_num
    if feedback_num > 0:
        if course_num <= 3:
            return feedback_num < course_num
        elif course_num > 3 and course_num <= 7:
            return feedback_num < course_num - 1
        else:
            return feedback_num < course_num - 2
    else:
        return False

def FinishCourse(item):
    if item.course_num <= 3:
        return item.feedback_forms.count() >= item.course_num
    elif item.course_num > 3 and item.course_num <= 7:
        return item.feedback_forms.count() >= item.course_num - 1
    else:
        return item.feedback_forms.count() >= item.course_num - 2


class NoFinishCourseListAPIView(ListAPIView):
    serializer_class = UserCourseSerializerTeacherInfo
    permission_classes = [AllowAny]

    def get_queryset(self):
        term = self.kwargs['term']

        return list(
            filter(
                lambda item: NoFinishCourse(item),
                UserCourse.objects.filter(
                    term_num=term,
                    is_fake=False
                )
            )
        )

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class FinishCourseListAPIView(ListAPIView):
    serializer_class = UserCourseSerializerTeacherInfo
    permission_classes = [AllowAny]

    def get_queryset(self):
        term = self.kwargs['term']

        return list(
            filter(
                lambda item: FinishCourse(item),
                UserCourse.objects.filter(
                    term_num=term
                )
            )
        )

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class SearchUserCourseListAPIView(ListAPIView):
    serializer_class = UserCourseSerializerTeacherInfo
    permission_classes = [AllowAny]

    def get_queryset(self):
        keyword = self.kwargs['keyword']
        term = self.kwargs['term']
        tag = self.kwargs['tag']

        teacherList = Teacher.objects.filter(
            Q(real_name__contains=keyword) |
            Q(phone__contains=keyword) |
            Q(name__contains=keyword),
            is_fake=False
        )

        userCourseList = []

        for teacher in teacherList:
            for userCourse in teacher.userCourses.all():
                userCourseList.append(userCourse)

        if tag == 'all':
            return list(
                filter(
                    lambda item: item.term_num == term and item.is_fake == False,
                    userCourseList
                )
            )
        else:
            return list(
                filter(
                    lambda item: item.term_num == term and item.tag_name == tag and item.is_fake == False,
                    userCourseList
                )
            )

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class UserCourseUpdateAPIView(UpdateAPIView):
    serializer_class = UserCourseSerializer
    permission_classes = [AllowAny]
    queryset = UserCourse.objects.all()

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class FeedbackPicCollectListAPIView(ListAPIView):
    serializer_class = FeedbackPicCollectSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        startDate = datetime.fromisoformat(self.kwargs['startDate'])
        endDate = datetime.fromisoformat(self.kwargs['endDate'])

        feedbackFormList = list(
            filter(
                lambda item: item.create_time >= startDate and item.create_time <= endDate,
                FeedbackForm.objects.all()
            )
        )

        feedbackPicList = []

        for form in feedbackFormList:
            for pic in form.feedback_pics.all():
                feedbackPicList.append(pic)

        return feedbackPicList

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
