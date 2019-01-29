# -*- coding: utf-8 -*-
from app import db
from flask_restplus import Api, Resource
from flask import jsonify, request
from app.v1_0 import v1_0
from app.model import User, Role, Perssion
from . import api


@api.route('/usernames')
class Usernames(Resource):
    def get(self):
        usernames = User.query.with_entities(User.name).all()
        return jsonify({
            "usernames": usernames
        })


@api.route('/users')
class Users(Resource):
    def get(self):
        users = User.query.all()
        return jsonify({
            "username"
        })


@api.route('/user_add')
class UserAdd(Resource):
    def post(self):
        pass
