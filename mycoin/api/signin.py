#coding: utf-8
from flask import jsonify , request
from .. import db
from ..models import User , Expend
from . import api

@api.route('/signin/',methods=['POST'])
def login() :
    un = request.get_json().get('username')
    passwd = request.get_json().get('password')
    user = User.query.filter_by(username=un).first()
    if not user :
        return jsonify ({}) , 403
    if not user.verify_password(passwd) :
        return jsonify ({}) , 401
    token = user.generate_auth_token()
    if len(Expend.query.filter_by(user_id=user.id).all()) == 0   :
        for i in range(2) :
            expend = Expend()
            expend.user_id = user.id
            expend.tag = 1
            db.session.add(expend)
            db.session.commit()
            ID = expend.id
            item = Expend.query.filter_by(id=ID).first()
            item.get_date(i+1)
            db.session.add(expend)
            db.session.commit()

    return jsonify({
        'token' : token ,
        }) , 200
