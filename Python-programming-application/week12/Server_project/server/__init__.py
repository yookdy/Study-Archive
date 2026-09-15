#처음 시작을 할 때 전개 및 서버를 초기화해주는 파일임

# project/server/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    #처음 서버가 시작이 될때
    app = Flask(__name__)
    app.config.from_object(Config) #Config를 import를 해서 필요한 부분만 사용을 한다는 의미

    db.init_app(app)

    from . import models
    from .views import main
    app.register_blueprint(main)
    #모델과 라우팅 등록

    with app.app_context():
        db.create_all()

    return app
