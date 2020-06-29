from django.contrib import admin

from .models import (
    Teacher,
    InfoForm,
    UserCourse,
    ApplyCourse,
    FeedbackForm,
    FeedbackUnit,
    FeedbackPic,
)

admin.site.register(Teacher)
admin.site.register(InfoForm)
admin.site.register(UserCourse)
admin.site.register(ApplyCourse)
admin.site.register(FeedbackForm)
admin.site.register(FeedbackUnit)
admin.site.register(FeedbackPic)
