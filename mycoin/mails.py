# coding: utf-8

from flask import render_template
from flask_mail import Message
from celery.utils.log import get_task_logger
from . import  app, celery_app, mails

logger = get_task_logger(__name__)

def msg_dict(to,subject,**kwargs):
    """
    生成邮件
    """
    msg = Message(
        subject=app.config['AUTH_MAIL_SUBJECT_PREFIX'] + ' ' + subject,
        sender=app.config['MAIL_DEFAULT_SENDER'],
        recipients=[to]
    )
    msg.body = render_template('signup.txt', **kwargs)
    msg.html = render_template('signup.html', **kwargs)
    return msg.__dict__

def send_mail(to, subject, **kwargs):
    """
    发送邮件
    """
    send_async_email.delay(msg_dict(to, subject, **kwargs))

@celery_app.task(default_retry_delay=30)
def send_async_email(msg_dict):
    with app.app_context():
        """
        异步方法
        """
        msg = Message()
        msg.__dict__.update(msg_dict)
        mails.send(msg)