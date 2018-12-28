# -*- coding: utf-8 -*-
from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class Perssion:
    """
    权限表
    """



class User(db.Model):
    """
    用户表
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError("password is not readable attribute")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<User {}>".format(self.username)


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(164), unique=True)
    default = db.Column(db.Integer)
    permission = db.Column(db.Integer)
    users = db.relationship('User', backref='role', lazy='dynamic')

    @staticmethod
    def insert_roles():
        """
        创建用户角色
        :return:
        """
        roles = {
            'User': ()
        }
