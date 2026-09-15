#라우팅을 설정을 해줌
# project/server/models.py
from . import db

class User(db.Model): #클래스를 상속을 받음
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=False, nullable=False) #이름수, 이름이 겹치는지, username이 없으면 에러
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self): #이름이 같은거 있을 때 오버라이딩 방지용
        return f"<User {self.username}>"
