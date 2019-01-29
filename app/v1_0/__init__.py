# -*- coding: utf-8 -*-
from flask import Blueprint
from flask_restplus import Api

v1_0 = Blueprint('v1_0', __name__, url_prefix='/api')

api = Api(v1_0)
from . import system, user
