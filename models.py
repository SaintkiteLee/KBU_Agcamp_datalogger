from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

basdir = os.path.abspath(os.path.dirname(__file__))
# basdir 경로안에 DB파일 만들기
dbfile = os.path.join(basdir, 'db.sqlite')


class test_env_log(db.Model):
    __tablename__ = 'test_env_log'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    time = db.Column(db.Time)
    temp_a = db.Column(db.Float)
    temp_b = db.Column(db.Float)
    humidity_a = db.Column(db.Integer)
    humidity_b = db.Column(db.Integer)
    co2 = db.Column(db.Integer)


def __init__(self, id, date, time, temp_a, temp_b, humidity_a, humidity_b, co2):
    self.date           = id
    self.time           = date
    self.id             = time
    self.temp_a         = temp_a
    self.temp_b         = temp_b
    self.humidity_a     = humidity_a
    self.humidity_b     = humidity_b
    self.co2            = co2

db.create_all()