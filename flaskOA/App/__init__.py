import os
from flask import Flask
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

base_dir=os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
bd_dir="sqlite:///"+os.path.join(base_dir,"OA.sqlite3")

template_dir=os.path.join(base_dir,"templates")
static_dir=os.path.join(base_dir,"static")

app=Flask(__name__,static_folder=static_dir,template_folder=template_dir)

app.config["SQLALCHEMY_DATABASE_URI"]=bd_dir
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=True
# app.config['SEND_FILE_MAX_AGE_DEFAULT']=timedelta(seconds=1)
# app.config['SECRET_KEY']=os.urandom(24)   #设置为24位的字符,每次运行服务器都是不同的，所以服务器启动一次上次的session就清除。
db=SQLAlchemy(app)