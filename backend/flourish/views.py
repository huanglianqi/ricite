from .models import (
    Teacher,
    InfoForm,
    UserCourse,
    UserCourseRemarks,
    ApplyCourse,
    FeedbackForm,
    FeedbackUnit,
    FeedbackPic,
    Share,
    SharePic,
)

from .serializers import (
    FeedbackPicCollectSerializer,
    ShareSrializer,
    ShareUpdateSerializer,
    UserCourseUpdateItemSerializer,
    ApplyCourseRetrieveSerializer,
    UserCourseAllListSerializer,
    UserCourseRemarksCreateSerializer,
    UserCourseRemarksDestroySerializer,
    UserCourseRemarksRetrieveSerializer,
    FeedbackFormRetrieveSerializer,
    TeacherInfoFormRetrieveSerializer
)

from rest_framework.generics import(
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    ListAPIView,
    RetrieveUpdateAPIView,
)

from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny
)

from rest_framework import filters

from django_filters.rest_framework import DjangoFilterBackend

from django.db.models import Q

from datetime import datetime

import pytz

from django.db.models import Q


# ---Teacher & Information Form--- #

class TeacherInfoFormRetrieveAPIView(RetrieveAPIView):
    serializer_class = TeacherInfoFormRetrieveSerializer
    permission_classes = [AllowAny]
    queryset = Teacher.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


# ---Feedback Form--- #

class FeedbackFormRetrieveAPIView(RetrieveAPIView):
    serializer_class = FeedbackFormRetrieveSerializer
    permission_classes = [AllowAny]
    queryset = FeedbackForm.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


# ---User Course--- #

class UserCourseListAPIView(ListAPIView):
    serializer_class = UserCourseAllListSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        term = self.kwargs['term']
        return UserCourse.objects.filter(
            term_num=term,
            is_fake=False
        )

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class UserCourseItemUpdateAPIView(UpdateAPIView):
    serializer_class = UserCourseUpdateItemSerializer
    permission_classes = [AllowAny]
    queryset = UserCourse.objects.all()

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class UserCourseRemarksCreateAPIView(CreateAPIView):
    serializer_class = UserCourseRemarksCreateSerializer
    permission_classes = [AllowAny]
    queryset = UserCourseRemarks.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserCourseRemarksDestroyAPIView(DestroyAPIView):
    serializer_class = UserCourseRemarksDestroySerializer
    permission_classes = [AllowAny]
    queryset = UserCourseRemarks.objects.all()

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class UserCourseRemarksRetrieveAPIView(RetrieveAPIView):
    serializer_class = UserCourseRemarksRetrieveSerializer
    permission_classes = [AllowAny]
    queryset = UserCourse.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


# ---Apply Course--- #

class ApplyCourseRetrieveAPIView(RetrieveAPIView):
    serializer_class = ApplyCourseRetrieveSerializer
    permission_classes = [AllowAny]
    queryset = ApplyCourse.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


# ---Feedback Image--- #

class FeedbackImageAllListAPIView(ListAPIView):
    serializer_class = FeedbackPicCollectSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        startDate = datetime.strptime(self.kwargs['startDate'], '%Y-%m-%dT%H:%M:%S').replace(tzinfo=pytz.utc)
        endDate = datetime.strptime(self.kwargs['endDate'], '%Y-%m-%dT%H:%M:%S').replace(tzinfo=pytz.utc)

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


class FeedbackImageLikeListAPIView(ListAPIView):
    serializer_class = FeedbackPicCollectSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        startDate = datetime.strptime(self.kwargs['startDate'], '%Y-%m-%dT%H:%M:%S').replace(tzinfo=pytz.utc)
        endDate = datetime.strptime(self.kwargs['endDate'], '%Y-%m-%dT%H:%M:%S').replace(tzinfo=pytz.utc)

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

        return list(
            filter(
                lambda item: item.like == True,
                feedbackPicList
            )
        )

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class FeedbackImageLikeUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = FeedbackPicCollectSerializer
    permission_classes = [AllowAny]
    queryset = FeedbackPic.objects.all()

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


# ---Share Graphic--- #

class ShareGraphicAllListAPIView(ListAPIView):
    serializer_class = ShareSrializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        startDate = datetime.strptime(self.kwargs['startDate'], '%Y-%m-%dT%H:%M:%S').replace(tzinfo=pytz.utc)
        endDate = datetime.strptime(self.kwargs['endDate'], '%Y-%m-%dT%H:%M:%S').replace(tzinfo=pytz.utc)

        return list(
            filter(
                lambda item: item.create_time >= startDate and item.create_time <= endDate,
                Share.objects.order_by('-create_time')
            )
        )

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ShareGraphicLikeListAPIView(ListAPIView):
   serializer_class = ShareSrializer
   permission_classes = [AllowAny]

   def get_queryset(self):
       startDate = datetime.strptime(self.kwargs['startDate'], '%Y-%m-%dT%H:%M:%S').replace(tzinfo=pytz.utc)
       endDate = datetime.strptime(self.kwargs['endDate'], '%Y-%m-%dT%H:%M:%S').replace(tzinfo=pytz.utc)

       return list(
           filter(
               lambda item: item.create_time >= startDate and item.create_time <= endDate and item.like,
               Share.objects.order_by('-create_time')
           )
       )

   def get(self, request, *args, **kwargs):
       return self.list(request, *args, **kwargs)


class ShareGraphicLikeUpdateAPIView(UpdateAPIView):
    serializer_class = ShareUpdateSerializer
    permission_classes = [AllowAny]
    queryset = Share.objects.all()

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
