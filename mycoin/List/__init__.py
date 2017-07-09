#!/usr/bin/env python
# encoding: utf-8
from flask import Blueprint
List = Blueprint(
    'List' ,
    __name__,
    template_folder = 'template' ,
    static_folder = 'static'
    )
from . import views
