from flask import jsonify
from flask_login import UserMixin
from . import db


def json_satuan(res):
    temp = {}
    for x in res.__table__.columns:
        temp[x.name] = getattr(res, x.name)
    return jsonify(data=temp)


def json_semua(res):
    list = []
    for x in res:
        temp = {}
        for y in x.__table__.columns:
            temp[y.name] = getattr(x, y.name)
        list.append(temp)
    return jsonify(data=list)


class User(db.Model, UserMixin):
    __tablename__ = "tb_user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), unique=True)
    password = db.Column(db.String(150))
    dob = db.Column(db.Date)
