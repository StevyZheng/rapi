# -*- coding: utf-8 -*-
from config import DatabaseConfig
from app import db
from flask_restplus import Api, Resource
from flask import jsonify, request

from app.v1_0 import v1_0


api_test = Api(v1_0)


@api_test.route('/test')
class Test(Resource):
    def get(self):
        return jsonify({
            "name": DatabaseConfig.NAME,
            "user": DatabaseConfig.USERNAME,
            "password": DatabaseConfig.PASSWORD
        })
