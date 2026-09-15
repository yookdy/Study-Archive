# from flask import Flask

# app=Flask(__name__)
# @app.route('/')
# def home():
#     return "Hello World!!"

# @app.route('/about_me')
# def about_me():
#     return '안녕하세요'

# if __name__=="__main__":
#     app.run(debug=True)


#파이썬을 이용을 한 데이터 베이스를 사용하기 Model을 이용을 함

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
import os

app = Flask(__name__)
# 데이터베이스 파일 경로 설정
BASE_DIR = os.path.abspath(os.path.dirname(__file__)) # 현재 경로 추출을 하고 BASE_DIR에 저장을 하는거임
DB_PATH = os.path.join(BASE_DIR, 'hello.db')#BASE_DIR의 뒤에 hello.db를 추가를 하는거임
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_PATH}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  #DB에서 필요함

db = SQLAlchemy(app)

class User(db.Model):#Model을 상속을 하는 의미
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    def __repr__(self):
        return f'<User {self.username}>'
    
@app.route('/')
def home():
    return render_template('index.html',name="World")


#with을 이용해서 파일을 마지막에 자동적으로 파일을 닫는걸로 설정을 함
if __name__ == "__main__":
 with app.app_context():
        db.create_all()
        app.run(debug=True)

#hello.db라는 파일이 생성이됨---임시 데이터베이스를 설정을 하는거임