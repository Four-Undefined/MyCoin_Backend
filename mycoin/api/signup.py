#coding: utf-8
from . import api
from .. import db
from flask import request , jsonify
from ..models import User
from ..mails import send_mail

@api.route('/signup/',methods=['POST'])
def signup() :
    un = request.get_json().get('username')
    passwd = request.get_json().get('password')
    if User.query.filter_by(username=un).first() is not None :
        return jsonify({}) , 401
    user = User(
        username = un ,
        password = passwd ,
        avatar = u"https://avatars2.githubusercontent.com/u/24372759?v=3&s=460"
        )
    db.session.add(user)
    db.session.commit()

    return jsonify({
        'create' : user.id ,
        }) , 200


@api.route('/signup/unique/',methods=['POST'])
def unique_signup():
    """
    用户名和邮箱查重
    发送邮件
    :return:
    """
    email = request.get_json().get('email')
    username = request.get_json().get('username')
    user = User.query.filter_by(email=email).first()
    if user is not None:
        return jsonify({
            'msg' : '邮箱已被注册！'
        }), 403
    user = User.query.filter_by(username=username).first()
    if user is not None:
        return jsonify({
            'msg' : '用户名已被注册！'
        }), 403

    captcha = '%06d' % (hash(username+email)%1000000)
    send_mail(email, 'MyCoin注册验证码',captcha=captcha)
    return jsonify({
        'msg' : '已发送邮件！',
    }), 200



@api.route('/signup/captcha/',methods=['POST'])
def check_captcha():
    """
    检查验证码
    注册用户
    :return:
    """
    email = request.get_json().get('email')
    username = request.get_json().get('username')
    password = request.get_json().get('password')
    captcha = request.get_json().get('captcha')
    real_captcha = '%06d' % (hash(username+email)%1000000)

    if captcha != real_captcha:
        return jsonify({
            'msg' : '验证码错误！',
        }), 401

    user = User(
        username = username ,
        password = password ,
        avatar = u"https://avatars2.githubusercontent.com/u/24372759?v=3&s=460",
        email = email,
        )

    db.session.add(user)
    db.session.commit()
    return jsonify({
        "msg" : "注册成功"
    }), 200
