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
)

from rest_framework.generics import(
    GenericAPIView,
    RetrieveAPIView,
    ListAPIView,
)
from rest_framework.mixins import (
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.permissions import (
    IsAuthenticated,
)

from rest_framework import filters

from django_filters.rest_framework import DjangoFilterBackend


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

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class InfoFormListAPIView(ListAPIView):
    queryset = InfoForm.objects.all()
    serializer_class = InfoFormSerializer
    permission_classes = [IsAuthenticated]
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
    permission_classes = [IsAuthenticated]
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
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        'user_id',
        'feedback_id'
    ]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class FeedbackPicRetrieveAPIView(RetrieveAPIView):
    queryset =FeedbackPic.objects.all()
    serializer_class = FeedbackPicSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)