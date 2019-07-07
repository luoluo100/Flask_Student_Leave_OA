from App import db
import hashlib

## student负责给学生申假，申请销假
class Student(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(32))
    age=db.Column(db.Integer)
    gender=db.Column(db.String(32))
    email = db.Column(db.String(32))
    phone=db.Column(db.String(32))
    password = db.Column(db.String)
    marital_status=db.Column(db.Integer) #0未婚 1已婚 2 离异 3 丧偶
    address=db.Column(db.Text)
    holiday=db.Column(db.String(32),default='false')
    grant = db.Column(db.Integer,default=0)  # 0代表学生权限

## 管理负责给学生批假
class Teacher(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(32))
    email = db.Column(db.String(32))
    password = db.Column(db.String(32))
    grant = db.Column(db.Integer, default=1) # 1代表老师权限

class Madmin(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(32))
    email = db.Column(db.String(32))
    password = db.Column(db.String(32))
    grant = db.Column(db.Integer,default=2)  # 2代表管理员