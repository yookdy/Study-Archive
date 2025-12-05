# project/run_server.py
# 전체적인 프로그램을 실행을 해주는 역활을 하고 있음
from server import create_app

app = create_app()

if __name__ == "__main__":
    app.run(port=8080, debug=True)
