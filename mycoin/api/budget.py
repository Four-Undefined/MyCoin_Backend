from flask import jsonify , request , g
from . import api
from .. import db
from ..models import User , Budget , Expend
from .decorators import login_required

@api.route("/budget/",methods=['POST'])
@login_required
def add_required() :
    budget = Budget (
            budget = request.get_json().get('budget') ,
            month = request.get_json().get('month') ,
            user_id = g.current_user.id  ,
            )
    db.session.add(budget)
    db.session.commit()
    return  jsonify ({
            "budget" : budget.to_json() ,
        }) , 200

@api.route('/view_budget/',methods=['POST'])
@login_required
def view_budget() :
    month = request.get_json().get('month')
    ID = g.current_user.id
    budget = Budget.query.filter_by(user_id=ID).filter_by(month=month).order_by("-id").first()
    if budget is None :
        budget = Budget(
            budget = 3000  ,
            month = request.get_json().get('month') ,
            user_id = g.current_user.id  ,
        )
        db.session.add(budget)
        db.session.commit()
    return  jsonify ({
            "budget" : budget.to_json() ,
        }) , 200

