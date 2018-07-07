#coding: utf-8
import requests
from flask import jsonify , request , g
from . import api
from ..models import Expend
from ..__init__ import db
from .decorators import login_required


@api.route('/add_account/',methods=['POST'])
@login_required
def add_comment() :
    """
    加账单
    """
    flag = 0
    month = request.get_json().get('month')
    day = request.get_json().get('day')
    user_id = g.current_user.id
    expend = Expend.query.filter_by(user_id=user_id).filter_by(month=month).filter_by(day=day).first()
    if expend is None :
        expend = Expend()
        expend.user_id = user_id
        flag = 1
    def choose(a,b) :
        print(a,b)
        if b == 0 :
            return max(a,0)
        return b

    expend.trip = choose(expend.trip,request.get_json().get('trip'))
    expend.edu = choose(expend.edu,request.get_json().get('edu'))
    expend.diet = choose(expend.diet,request.get_json().get('diet'))
    expend.normal = choose(expend.normal,request.get_json().get('normal'))
    expend.clothes = choose(expend.clothes,request.get_json().get('clothes'))
    expend.enter = choose(expend.enter,request.get_json().get('enter'))
    expend.month = month
    expend.day = day
    expend.get_date()
    expend.tag = 1
    expend.get_sum()

    if flag == 1 :
        db.session.add(expend)

    db.session = db.session.object_session(expend)
    db.session.commit()

    return jsonify({
            'expend' : expend.to_json1() ,
        }) , 200


@api.route('/get_day/',methods=['POST'])
@login_required
def get_day():
    month = request.get_json().get('month')
    day = request.get_json().get('day')
    user_id = g.current_user.id
    expend = Expend.query.filter_by(user_id=user_id).filter_by(month=month).filter_by(day=day).first()
    return jsonify({
        'expend': expend.to_json1(),
    }), 200

@api.route('/get_two/',methods=['GET'])
@login_required
def get_two():
    three = Expend.query.filter_by(user_id=g.current_user.id).filter_by(tag=1).order_by("-id").limit(2).all()
    return jsonify({
        'expend': [ expend.to_json() for expend in three],
    }), 200

@api.route('/get_seven/',methods=['GET'])
@login_required
def get_seven() :
    seven = Expend.query.filter_by(user_id=g.current_user.id).filter_by(tag=1).order_by("-id").limit(7).all()
    List = [0,0,0,0,0,0,0 ]
    List2 = ['教育','一般','饮食','出行','娱乐','服饰','sumup']
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
    List2 = ['教育','一般','饮食','出行','娱乐','服饰','sumup']
    maxDay = one[0]
    List = [0,0,0,0,0,0,0]
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
            "result" : [ { "class" : i ,"expend" : j } for i , j in zip(List2[:6],List[:6])] ,
            "MaxClass" : Max ,
            "maxExpend" : maxExpend ,
            "TotalExpend" : List[6] ,
        }) , 200

@api.route('/get_some/',methods=['GET'])
@login_required
def get_some() :
    each = Expend.query.filter_by(user_id=g.current_user.id).order_by('-id').limit(1).first()
    print(each)
    List = [0,0,0,0,0,0,0 ]
    List2 = ['教育','一般','饮食','出行','娱乐','服饰','sumup']
    List[0] += each.edu
    List[1] += each.normal
    List[2] += each.diet
    List[3] += each.trip
    List[4] += each.enter
    List[5] += each.clothes
    List[6] += each.sumup

    return jsonify({
            "result" : [{ "class" : i , "expend" : j } for i , j in zip(List2,List)]  ,
        }) , 200

@api.route('/get_one/<int:month>/',methods=['GET'])
@login_required
def get_one(month) :
    one = Expend.query.filter_by(month=month).filter_by(user_id=g.current_user.id).all()
    sumup = 0
    for each in one :
        sumup += each.sumup
    return jsonify({
            "sum" : sumup ,
        }) , 200


@api.route('/card/',methods=['GET'])
def card():
    """
    获取到校园卡账单信息
    :return:
    """
    stime = request.args.get('time')
    sid = request.args.get('sid')
    url = 'http://weixin.ccnu.edu.cn/App/weixin/queryTrans'
    headers = {
        "Content - Type": "application/json",
        "Cookie": "ASP.NET_SessionId=xmc4qqukczkz1ljlxtsteaqb; wxqyuserid=%s" % sid,
    }
    params = {
        "page": 1,
        "pageSize": 200,
        "startTime": stime,
        "endTime": stime,
    }
    r = requests.get(url,params=params,headers=headers)

    return jsonify({
        'response' : r.json(),
    }) ,200
