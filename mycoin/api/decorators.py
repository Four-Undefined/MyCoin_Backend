#coding: utf-8
from functools import wraps
from flask import abort , g , jsonify , request
from ..models import User

def login_required(f) :
    @wraps(f)
    def decorated(*args,**kwargs) :
        token = request.headers.get('token')
        if token is not None :
            g.current_user = User.verify_auth_token(token)
            return f(*args,**kwargs)
        return jsonify("login first!") , 401
    return decorated

