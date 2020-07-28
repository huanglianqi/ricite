from __future__ import (
    absolute_import,
    unicode_literals
)

from celery import shared_task
from celery.task.schedules import crontab
from celery.decorators import periodic_task

from .models import (
    Teacher,
    InfoForm,
    UserCourse,
    ApplyCourse,
    FeedbackForm,
    FeedbackUnit,
    FeedbackPic,
    Share,
    ShareComment,
    SharePic,
    ShareLike,
)

from datetime import datetime

from django.utils.timezone import get_current_timezone

import requests, json


def strToDate(strTime):
    if strTime == None:
        return None
    else:
        return get_current_timezone().localize(
            datetime.strptime(
                strTime,
                '%Y-%m-%d %H:%M:%S'
            )
        )



BASE_URL = 'http://www.rici.org.cn/rici/api/'

# method: get
# params: null
# data: {token}
GET_API_TOKEN = BASE_URL + 'get_api_token'

# method: get
# params: {page: <int>, limit: <int>}
# if not params, default page is 0, default limit is 50
# data: {user_id, name, real_name, phone, head_img, create_time}
# name means wechat name, real_name means personal ID card's name
GET_USER_LIST = BASE_URL + 'get_user_list'

# method: get
# params: {user_id: <int>}
# data: {user_course_id, tag_name, tag_label, rag_desc, course_num, tag_cover}
# tag means courses in flourish magic academy project
GET_USER_COURSE = BASE_URL + 'get_user_course'

# method: get
# params: {user_course_id: <int>}
# data: {stu_num, teacher_num, front_img, back_img, school_name, school_address}
# front_img and back_img means personal ID card pic
GET_USER_PROTOCAL = BASE_URL + 'get_user_protocal'

# method: get
# params: {user_id: <int>}
# data: -> <list:> {field_id, field_name, field_value, create_time}
# field means question and answer in personal info form
GET_USER_INFO_FORM = BASE_URL + 'get_user_info_form'

# mehtod: get
# params: {user_course_id: <int>}
# data: {code: 0, msg: 'success', data: [{"0": {
# field_id, field_value, field_name}}]}
# field means courses feedback form
GET_CLASS_FORM_INFO = BASE_URL + 'get_class_form_info'

# method: get
# params: {page: <int>}
# data: {code: 0, msg: 'success', data: [{uid, username, name, groupid, reg_time, last_login_time}]}
GET_SHARE_LIST = BASE_URL + 'get_share_list'

res_token = requests.get(GET_API_TOKEN)

HEADERS = {
    'Token': res_token.json()['data']['token']
}


@shared_task
@periodic_task(
    run_every=(
        crontab(
            minute=0,
            hour='*/3'
        )
    ),
    name="Update_Share_List",
    ignore_result=True
)
def Update_share_list(page=0):
    """
    Each 3 Hour, Update db for share list,
    If not exits, create a new instant;
    If exits, update certain instant.
    """
    res_data = requests.get(
        '{0}?page{1}'.format(
            GET_SHARE_LIST,
            page
        ),
        headers=HEADERS
    )
    data = res_data.json()['data']
    for item in data:
        try:
            instant = Share.objects.get(
                moment_id=item['moment_id']
            )
            try:
                for comment in item['comments']:
                    try:
                        c = ShareComment.objects.get(
                            teacher__user_id=comment['user_id']
                        )
                    except ShareComment.DoesNotExist:
                        try:
                            c = ShareComment(
                                content=comment['content'],
                                teacher=Teacher.objects.get(user_id=comment['user_id']),
                                share=instant,
                                user_id=commnet['user_id'],
                                user_name=commnet['user_name'],
                                user_real_name=commnet['user_real_name']
                            )
                            c.save()
                        except Teacher.DoesNotExist:
                            print('This teacher may has been delated')
            except KeyError:
                    print('Not exist comments')
            try:
                for like in item['likes']:
                    try:
                        l = ShareLike.objects.get(
                            user_id=like['user_id']
                        )
                    except ShareLike.DoesNotExist:
                        try:
                            l = ShareLike(
                                teacher=Teacehr.objects.get(
                                    user_id=like['user_id']
                                ),
                                share=instant,
                                user_id=like['user_id'],
                                user_name=like['user_name'],
                                user_real_name=like['user_real_name']
                            )
                            l.save()
                        except Teacher.DoesNotExist:
                            print(item)
            except KeyError:
                print('Not exist likes')
        except Share.DoesNotExist:
            instant = Share(
                like=False,
                user_id=item['user_id'],
                moment_id=item['moment_id'],
                content=item['content'],
                create_time=item['create_time']
            )
            instant.save()
            try:
                for comment in item['comments']:
                    try:
                        c = ShareComment.objects.get(
                            teacher__user_id=comment['user_id']
                        )
                    except ShareComment.DoesNotExist:
                        try:
                            c = ShareComment(
                                content=comment['content'],
                                teacher=Teacher.objects.get(user_id=comment['user_id']),
                                share=instant,
                                user_id=commnet['user_id'],
                                user_name=commnet['user_name'],
                                user_real_name=commnet['user_real_name']
                            )
                            c.save()
                        except Teacher.DoesNotExist:
                            print('This teacher may has been deleted')
            except KeyError:
                print('Not exist comments')
            try:
                for like in item['likes']:
                    try:
                        l = ShareLike.objects.get(
                            user_id=like['user_id']
                        )
                    except ShareLike.DoesNotExist:
                        try:
                            l = ShareLike(
                                teacher=Teacehr.objects.get(
                                    user_id=like['user_id']
                                ),
                                share=instant,
                                user_id=like['user_id'],
                                user_name=like['user_name'],
                                user_real_name=like['user_real_name']
                            )
                            l.save()
                        except Teacher.DoesNotExist:
                            print('This teacher may has been deleted')
            except KeyError:
                print('Not exist likes')
            try:
                for pic in item['pics']:
                    sharePic = SharePic(
                        url=pic,
                        belongTo=instant,
                        like=False
                    )
                    sharePic.save()
            except KeyError:
                print('Not exist pics')
    if len(data) == 100:
        page += 1
        Update_share_list(page)


@shared_task
@periodic_task(
    run_every=(
        crontab(
            minute=0,
            hour=0
        )
    ),
    name="Update_Teacher_Info",
    ignore_result=True
)
def update_teacher_info():
    """
    Every MIDNIGHT update database for app flourish,
    If not exits, create a new instant;
    If exits, update certain instant.
    """
    # get data num -> <int: data_num>
    res_data_num = requests.get(
        GET_USER_LIST,
        headers=HEADERS,
        params={
            'limit': 0
        }
    )
    data_num = int(
        res_data_num.json()['data']['total_count']
    )

    # get all data -> <list: data>
    res_data = requests.get(
        GET_USER_LIST,
        headers=HEADERS,
        params={
            'limit': data_num
        }
    )
    data = res_data.json()['data']['data']

    # create or update teacher info
    for item in data:
        try:
            instant = Teacher.objects.get(
                user_id=item['user_id']
            )
            instant.name = item['name']
            instant.real_name = item['real_name']
            instant.phone = item['phone']
            instant.head_img = item['head_img']
            instant.save()
        except Teacher.DoesNotExist:
            instant = Teacher(
                user_id=item['user_id'],
                name=item['name'],
                real_name=item['real_name'],
                phone=item['phone'],
                head_img=item['head_img'],
                create_time=strToDate(
                    item['create_time']
                ),
                is_active=False,
                has_course=False,
                is_reapply=False,
                is_fake=False
            )
            instant.save()

    for teacher in Teacher.objects.all():
        # update user info form
        res_info_form = requests.get(
            GET_USER_INFO_FORM,
            headers=HEADERS,
            params={
                'user_id': int(teacher.user_id)
            }
        )
        info_form = res_info_form.json()['data']
        if info_form == None or info_form == []:
            teacher.is_active = False
            teacher.save()
        else:
            teacher.is_active = True
            teacher.save()
            for item in info_form:
                try:
                    instant = InfoForm.objects.get(
                        user_id=item['user_id'],
                        field_id=item['field_id']
                    )
                    instant.field_name = item['field_name']
                    instant.field_value = item['field_value']
                    instant.save()
                except InfoForm.DoesNotExist:
                    instant = InfoForm(
                        field_id=item['field_id'],
                        field_name=item['field_name'],
                        field_value=item['field_value'],
                        create_time=strToDate(
                            item['create_time']
                        ),
                        user_id=item['user_id'],
                        teacher=teacher
                    )
                    instant.save()

        # update user course list
        res_user_course = requests.get(
            GET_USER_COURSE,
            headers=HEADERS,
            params={
                'user_id': int(teacher.user_id)
            }
        )
        user_course = res_user_course.json()['data']
        if user_course == None or user_course == []:
            continue
        else:
            for item in user_course:
                try:
                    instant = UserCourse.objects.get(
                        user_course_id=item['user_course_id']
                    )
                    instant.tag_name=item['tag_name']
                    instant.course_num=item['course_num']
                    instant.term_num=item['term_num']
                    teacher.save()
                except UserCourse.DoesNotExist:
                    instant = UserCourse(
                        user_course_id=item['user_course_id'],
                        user_id=teacher.user_id,
                        tag_name=item['tag_name'],
                        course_num=int(item['course_num']),
                        term_num=item['term_num'],
                        teacher=teacher
                    )
                    instant.save()

    for apply in UserCourse.objects.all():
        res_apply_course = requests.get(
            GET_USER_PROTOCAL,
            headers=HEADERS,
            params={
                'user_course_id': int(apply.user_course_id)
            }
        )
        apply_course = res_apply_course.json()['data']
        if apply_course == None or apply_course == []:
            teacher.has_course = False
            teacher.is_reapply = False
            teacher.save()
        else:
            teacher.has_course = True
            teacher.save()
            if len(apply_course) >= 2:
                teacher.is_reapply = True
                teacher.save()
            else:
                teacher.is_reapply = False
                teacher.save()
            try:
                instant = ApplyCourse.objects.get(
                    _user_course_id=apply.user_course_id
                )
                instant.stu_num = apply_course['stu_num']
                instant.teacher_num = apply_course['teacher_num']
                instant.front_img = apply_course['front_img']
                instant.back_img = apply_course['back_img']
                instant.school_name = apply_course['school_name']
                instant.school_address = apply_course['school_address']
                instant.save()
            except ApplyCourse.DoesNotExist:
                instant = ApplyCourse(
                    stu_num=apply_course['stu_num'],
                    teacher_num=apply_course['teacher_num'],
                    front_img=apply_course['front_img'],
                    back_img=apply_course['back_img'],
                    school_name=apply_course['school_name'],
                    school_address=apply_course['school_address'],
                    _user_course_id=apply.user_course_id,
                    user_id=apply.user_id,
                    user_course=apply,
                    teacher=apply.teacher
                )
                instant.save()

        # update feedback form
        res_feedback_form = requests.get(
            GET_CLASS_FORM_INFO,
            headers=HEADERS,
            params={
                'user_course_id': int(apply.user_course_id)
            }
        )
        feedback_form = res_feedback_form.json()['data']
        if feedback_form == None or feedback_form == []:
            continue
        else:
            for form in feedback_form:
                try:
                    instant = FeedbackForm.objects.get(
                        feedback_id=form['id']
                    )
                except FeedbackForm.DoesNotExist:
                    instant = FeedbackForm(
                        feedback_id=form['id'],
                        create_time=strToDate(
                            form['create_time']
                        ),
                        class_num=form['class_num'],
                        _user_course_id=apply.user_course_id,
                        user_id=apply.user_id,
                        user_course=apply,
                        teacher=apply.teacher
                    )
                    instant.save()
                pic_url_list = form['feedback_pic'].split(',')
                for pic_url in pic_url_list:
                    try:
                        instant = FeedbackPic.objects.get(
                            pic_url=pic_url
                        )
                    except FeedbackPic.DoesNotExist:
                        instant = FeedbackPic(
                            pic_url=pic_url,
                            feedback_id=form['id'],
                            _user_course_id=apply.user_course_id,
                            user_id=apply.user_id,
                            feedback_form=FeedbackForm.objects.get(
                                feedback_id=form['id']
                            ),
                            user_course=apply,
                            teacher=apply.teacher
                        )
                        instant.save()
                for item in range(len(form)-4):
                    unit = form[str(item)]
                    try:
                        instant = FeedbackUnit.objects.get(
                            field_id=unit['field_id'],
                            feedback_id=form['id']
                        )
                        instant.field_name = unit['field_name']
                        instant.field_value = unit['field_value']
                        instant.save()
                    except FeedbackUnit.DoesNotExist:
                        instant = FeedbackUnit(
                            field_id=unit['field_id'],
                            field_name=unit['field_name'],
                            field_value=unit['field_value'],
                            feedback_id=form['id'],
                            _user_course_id=apply.user_course_id,
                            user_id=apply.user_id,
                            feedback_form=FeedbackForm.objects.get(
                                feedback_id=form['id']
                            ),
                            user_course=apply,
                            teacher=apply.teacher
                        )
                        instant.save()
