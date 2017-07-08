#coding: utf-8
from flask import jsonify , request , g
from . import api
from .. import db
from ..models import User
from .decorators import login_required


@api.route("/profile/",methods=['PUT'])
@login_required
def edit_profile() :
    """
    改头像
    """
    ID = g.current_user.id
    user = User.query.filter_by(id=ID).first()
    avatar = request.get_json().get('avatar')
    db.session.add(user)
    db.session.commit()
    return jsonify ({
            "avatar" : avatar ,
        }) , 200

@api.route("/show_profile/",methods=['GET'])
@login_required
def show() :
    ID = g.current_user.id
    user = User.query.filter_by(id=ID).first()
    return jsonify({
            "username" : user.username ,
        }) , 200
