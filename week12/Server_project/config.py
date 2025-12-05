#설정을 관리하는 파일
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = "dev-secret-key"
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'hello1.db')}"#hello.db를 생성을 함
    SQLALCHEMY_TRACK_MODIFICATIONS = False #