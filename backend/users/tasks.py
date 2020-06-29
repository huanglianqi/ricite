from __future__ import (
    absolute_import,
    unicode_literals
)

from celery import shared_task
from celery.task.schedules import crontab
from celery.decorators import periodic_task

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from .models import SubscribeEmail


def post_mail(
    pk,
    title,
    main_content
):
    subscribers = SubscribeEmail.objects.get(pk=pk).subscriber.all()
    for subscriber in subscribers:
        content = {
            'lastname': subscriber.last_name,
            'firstname': subscriber.first_name,
            'email': subscriber.email,
            'title': title
        }
        for k, v in main_content.items():
            content[k] = v

        email_html_message = render_to_string(
            'subscribe_email.html',
            content
        )
        msg = EmailMultiAlternatives(
            '日慈信息管理平台 | {0}'.format(
                title
            ),
            title,
            'huanglianqi@ricifoundation.com',
            [subscriber.email]
        )
        msg.attach_alternative(
            email_html_message,
            'text/html'
        )
        msg.send()


def base_post(
    pk,
    title
):
    content = {} # sepcial content data need to add When get API !!!
    post_mail(
        pk=pk,
        title=title,
        main_content=content
    )


def feedback_post(
    pk,
    title
):
    content = {}  # sepcial content data need to add When get API !!!
    post_mail(
        pk=pk,
        title=title,
        main_content=content
    )


@shared_task
@periodic_task(
    run_every=(
        crontab(
            minute=30,
            hour=8
        )
    ),
    name="Post_Daily",
    ignore_result=True
)
def post_daily():
    base_post(
        pk=1,
        title='小慈日报'
    )
    feedback_post(
        pk=4,
        title='反馈日报'
    )

@shared_task
@periodic_task(
    run_every=(
        crontab(
            minute=30,
            hour=8,
            day_of_week='mon'
        )
    ),
    name="Post_Weekly",
    ignore_result=True
)
def post_weekly():
    base_post(
        pk=2,
        title='小慈周报'
    )
    feedback_post(
        pk=5,
        title='反馈周报'
    )

@shared_task
@periodic_task(
    run_every=(
        crontab(
            minute=30,
            hour=8,
            day_of_month='1'
        )
    ),
    name="Post_Monthly",
    ignore_result=True
)
def post_monthly():
    base_post(
        pk=3,
        title='小慈月报'
    )
    feedback_post(
        pk=6,
        title='反馈月报'
    )
