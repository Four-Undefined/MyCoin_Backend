#coding: utf-8
from . import api
from .. import db
from flask import request , jsonify
from ..models import User , Expend

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
