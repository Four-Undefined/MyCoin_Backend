#coding: utf-8
from flask import jsonify , request , g
from . import api
from ..models import User , Expend
from ..__init__ import db
from .decorators import login_required

@api.route('/add_account/',methods=['POST'])
@login_required
def add_comment() :
    """
    加账单
    """
    expend = Expend()
    expend.user_id = g.current_user.id
    expend.trip = request.get_json().get('trip')
    expend.edu = request.get_json().get('edu')
    expend.diet = request.get_json().get('diet')
    expend.normal = request.get_json().get('normal')
    expend.clothes = request.get_json().get('clothes')
    expend.enter = request.get_json().get('enter')
    expend.tag = 1
    expend.get_sum()
    db.session.add(expend)
    db.session.commit()
    ID = expend.id
    item = Expend.query.filter_by(id=ID).first()
    item.get_date(0)
    db.session.add(item)
    db.session.commit()

    return jsonify({
            'expend' : expend.to_json1() ,
        }) , 200


@api.route('/get_seven/',methods=['GET'])
@login_required
def get_seven() :
    seven = Expend.query.filter_by(user_id=g.current_user.id).filter_by(tag=1).order_by("-id").limit(7).all()
    List = [0,0,0,0,0,0,0 ]
    List2 = ['edu','normal','diet','trip','enter','clothes','sumup']
    maxDay = seven[0]
    for each in seven :
        if each.sumup > maxDay.sumup :
            maxDay  = each
        List[0] += each.edu
        List[1] += each.normal
        List[2] += each.diet
        List[3] += each.trip
        List[4] += each.enter
        List[5] += each.clothes
        List[6] += each.sumup

    return jsonify({
            "sumup" : [ expend.to_json2() for expend in seven ] ,
            "maxDay" : maxDay.to_json2() ,
            "result" : [ { "class" : i , "expend" : j } for i , j in zip(List2[:6],List[:6])] ,
            "TotalExpend" : List[6] ,
        }) , 200

@api.route('/get_month/<int:month>/',methods=['GET'])
@login_required
def get_month(month) :
    one = Expend.query.filter_by(month=month).filter_by(user_id=g.current_user.id).all()
    List = [0,0,0,0,0,0,0]
    List2 = ['edu','normal','diet','trip','enter','clothes','sumup']
    List3 = []
    for each in one :
        List[0] += each.edu
        List[1] += each.normal
        List[2] += each.diet
        List[3] += each.trip
        List[4] += each.enter
        List[5] += each.clothes
        List[6] += each.sumup

    maxExpend = max(List[:6])
    for i , j in enumerate(List) :
        if j == maxExpend :
            Max = List2[i]
            break

    return jsonify({
            "result" : [ { "class" : i ,"expend" : j } for i , j in zip(List2,List)] ,
            "MaxClass" : Max ,
            "maxExpend" : maxExpend ,
        }) , 200

