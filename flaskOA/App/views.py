from App import db,app
from flask import render_template,url_for
from flask import request,redirect
from App.models import Student,Madmin,Teacher
session=db.session


@app.route("/login",methods=["get","post"])
def login():
    if request.method == "POST":
        email = request.form.get("username")
        pwd = request.form.get('password')
        inf = session.query(Madmin).filter(Madmin.email==email).first()  # flask 使用query查询不用objects
        inf2 = session.query(Teacher).filter(Teacher.email==email).first()  # flask 使用query查询不用objects
        inf3 = session.query(Student).filter(Student.email==email).first()  # flask 使用query查询不用objects
        if inf:
            inf=inf
        elif inf2:
            inf=inf2
        elif inf3:
            inf = inf3
        # print(inf)
        if inf:
            if inf.password == pwd:
                # print(inf.password)
                response =  redirect('/')

                response.set_cookie(key='user', value=inf.name,max_age=7 * 24 * 3600) # user是key，names是value，max_age是生存周期
                return response
        else:
            message = "用户名或者密码错误"
            return render_template('login.html',message=message)
    return render_template('login.html')


#退出系统
@app.route('/out',methods=['GET','POST'])
def out():
    response = redirect('/')
    #通过response删除cookie里的'user'
    response.delete_cookie('user')
    return response


@app.route("/",methods=['GET','POST'])  #登陆后的导航页，学生老师共用此页面
def index():
    student_list=Student.query.all()
    username = request.cookies.get("user","")  ##  如果user没取到，求设置user的值为""
    # print(username)

    if username:
        # print(username)
        grant1 = session.query(Madmin).filter(Madmin.name==username).first()
        grant2 = session.query(Teacher).filter(Teacher.name==username).first()
        grant3 = session.query(Student).filter(Student.name==username).first()
        if grant1:
            grant = grant1.grant
        elif grant2:
            grant = grant2.grant
        elif grant3:
            grant = grant3.grant
        # print(grant)
        return render_template("blank.html",students=student_list,username=username,student=grant)
    return  redirect('/login')


@app.route("/addStudent/",methods=["get","post"])  # 添加学生
def addStudent():
    if request.method=="POST":
        name=request.form.get("name")
        age=int(request.form.get("age"))
        gender=request.form.get("gender")
        email = request.form.get("email")
        phone=request.form.get("phone")
        address=request.form.get("address")
        marital_status=int(request.form.get("mariy"))
        student=Student(name=name,age=age,email=email,password=phone,gender=gender,phone=phone,address=address,marital_status=marital_status)
        session.add(student) #session服务器段保存用户信息
        session.commit()
        return redirect("/")
    return render_template("addStudent.html")


@app.route("/yiqingjia/")  # 已请假
def yiqingjia():
    student_list=Student.query.filter_by(holiday='true')
    return render_template("studentx.html", students=student_list)

@app.route("/weiqingjia/")
def weiqingjia():
    student_list = Student.query.filter_by(holiday='false')
    return render_template("studentq.html", students=student_list)

@app.route("/daipizhun/")
def daipizhun():
    student_list = Student.query.filter_by(holiday='waiting')
    return render_template("studentd.html", students=student_list)

@app.route("/qingjia/<id>/")
def qingjia(id):
    stu=Student.query.get(id)
    stu.holiday='waiting'
    session.commit()
    return redirect("/daipizhun/")

@app.route("/xj/<id>/")
def xj(id):
    stu=Student.query.get(id)
    stu.holiday='false'
    session.commit()
    return redirect("/weiqingjia/")

@app.route("/pizhun/")
def pizhun():
    student_list=Student.query.filter_by(holiday='waiting')
    # print(student_list)
    return render_template('pizhun.html',students=student_list)

@app.route("/pj/<id>/")
def pj(id):
    stu=Student.query.get(id)
    stu.holiday='true'
    session.commit()
    return redirect("/yiqingjia/")

@app.route("/qx/<id>/")
def qx(id):
    stu=Student.query.get(id)
    stu.holiday='false'
    session.commit()
    return redirect("/weiqingjia/")






