# project/server/views.py
#서버의 역활을 하고 있음
from flask import Blueprint, render_template, request, redirect, url_for
from . import db
from .models import User

main = Blueprint("main", __name__)

@main.route("/", methods=["GET"])#메인의 루트로 설정을 해준거임
def index():
    return render_template("index.html")

@main.route("/submit", methods=["POST"])
def submit():
    username = request.form.get("username")#get으로 받아오는 역활을 함
    email = request.form.get("email")

    new_user = User(username=username, email=email) #객체를 생성을 해서 각각에 넣는거임
    db.session.add(new_user) #세션을 호출을해서 db하고 웹하고 연결을 해주는거임-- 통로에 user를 넣어주는역활
    db.session.commit() #commit을 실행을 해서 user를 db에 넣는다는의미

    return redirect(url_for("main.result", username=username, email=email))

@main.route("/result", methods=["GET"])# sumit을 누르면 해당되는 주소 이용을 한다는 의미
def result():
    username = request.args.get("username")
    email = request.args.get("email")
    return f"User {username} with email {email} has been added to the database."
