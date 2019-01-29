# -*- coding: utf-8 -*-
from app import db
from flask_restplus import Api, Resource
from flask import jsonify, request
from app.v1_0 import v1_0
from libs.system import Common
from . import api


@api.route('/sysinfo')
class Sysinfo(Resource):
    def get(self):
        tmp = Common.shell_exec("cat /etc/redhat-release").strip()
        return jsonify({
            "os": tmp
        })
