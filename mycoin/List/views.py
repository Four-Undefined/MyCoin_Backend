#!/usr/bin/env python
# encoding: utf-8

from . import List
from ..api import api
from flask import render_template, url_for, redirect, flash, session, request

@List.route('/get_seven/',methods=['GET'])
def seven() :
    return render_template('week/week.html')

@List.route('/get_month/',methods=['POST','GET'])
def month() :
    return render_template('month.html')

@List.route('/get_list/',methods=['POST','GET'])
def Lists() :
    return render_template('list.html')

