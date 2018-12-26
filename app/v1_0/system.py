# -*- coding: utf-8 -*-
from app import db
from flask_restplus import Api, Resource
from flask import jsonify, request
from app.v1_0 import v1_0
from libs.system import Common

api_system = Api(v1_0)


@api_system.route('/sysinfo')
class Test(Resource):
    def get(self):
        tmp = Common.shell_exec("cat /etc/redhat-release").strip()
        return jsonify({
            "os": tmp
        })
