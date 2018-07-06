#coding: utf-8
from  flask import current_app , request
from . import db
from werkzeug.security import generate_password_hash , check_password_hash
from itsdangerous import JSONWebSignatureSerializer as Serializer
from flask_login import UserMixin,  current_user
from datetime import datetime

class User(db.Model, UserMixin) :
    """
    user
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    avatar = db.Column(db.String(164),default="1")
    username = db.Column(db.String(20),unique=True,index=True)
    email = db.Column(db.String(40),unique=True)
    signup_t = db.Column(db.String(20))
    password_hash = db.Column(db.String(164))
    expends = db.relationship('Expend',backref='user',lazy='dynamic')
    budgets = db.relationship('Budget',backref='user',lazy='dynamic')

    @property
    def password(self) :
        raise AttributeError('password is not readable')

    @password.setter
    def password(self,password) :
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password) :
        return check_password_hash(self.password_hash,password)

    @staticmethod
    def verify_auth_token(token) :
        s = Serializer(current_app.config['SECRET_KEY'])
        try :
            data = s.loads(token)
        except :
            None
        return User.query.get_or_404(data['id'])

    def generate_auth_token(self) :
        s = Serializer(
            current_app.config['SECRET_KEY']
        )
        return s.dumps({'id' : self.id})

    @staticmethod
    def from_json(json_user) :
        u = User(
            username = json_user.get('username') ,
            password = json_user.get('password')
        )
        return u

class Expend(db.Model) :
    __tablename__ = 'expend'
    id = db.Column(db.Integer,primary_key=True)
    timestamp = db.Column(db.DateTime,index=True,default=datetime.utcnow)
    date = db.Column(db.String(10),default="1")
    day = db.Column(db.Integer,default=0)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    trip = db.Column(db.Float,default=0)
    edu = db.Column(db.Float,default=0)
    diet = db.Column(db.Float,default=0)
    enter = db.Column(db.Float,default=0)
    clothes = db.Column(db.Float,default=0)
    normal = db.Column(db.Float,default=0)
    sumup = db.Column(db.Float,default=0)
    month = db.Column(db.Integer,default=1)
    tag = db.Column(db.Integer)

    def get_sum(self) :
        self.sumup = self.trip + self.edu + self.diet + self.enter + self.clothes + self.normal

    def get_date(self) :
        self.date = u"%s月%d日" % (self.month,self.day)

    def to_json1(self) :
        json_expend = {
            'id' : self.id ,
            'sum' : self.sumup ,
            'date' : self.date
        }
        return json_expend

    def to_json2(self) :
        json_expend = {
                'date' : self.date ,
                'expend' : self.sumup ,
                'id' : self.id ,
        }
        return json_expend

    def to_json(self) :
        json_expend = {
                    '教育' : self.edu ,
                    '一般' : self.normal ,
                    '饮食' : self.diet ,
                    '出行' : self.trip ,
                    '娱乐' : self.enter ,
                    '服饰' : self.clothes ,
                    '总和' : self.sumup ,
                    '日期' : self.date ,
                }
        return json_expend

class Budget(db.Model) :
    __tablename__ = 'budget'
    id = db.Column(db.Integer,primary_key=True)
    budget = db.Column(db.Integer,default=0)
    month = db.Column(db.Integer,default=0)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

    def to_json(self) :
        json_budget = {
                'budget' : self.budget ,
                'month' : self.month ,
                'user_id' : self.user_id ,
                }
        return json_budget
