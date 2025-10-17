import tkinter as tk
import random

class ShootingGame:
    def __init__(self):
        # 게임을 표시할 윈도우 생성 / 제목 표시
        self.window = tk.Tk()
        self.window.title("Shooting Game")

        # 게임이 실행되는 영역(배경화면) 생성
        self.width = 400
        self.height = 600
        self.canvas = tk.Canvas(
            master=self.window,  # 부모 객체 이름
            width=self.width,    # 캔버스 가로 크기(픽셀)
            height=self.height,  # 캔버스 세로 크기(픽셀)
            bg="black"           # 배경색
        )
        self.canvas.pack()

        # 플레이어 생성
        self.player = self.canvas.create_rectangle(180, 580, 220, 600, fill="blue")
        self.bullets = [] # 총알을 담아 놓을 리스트
        self.enemies = [] # 적을 담아 놓을 리스트
        self.score = 0    # 적을 맞췄을 때 점수

        # 키보드에서 화살표 키를 눌렀을 때 작동할 함수 등록
        self.window.bind("<Left>", self.move_left)
        self.window.bind("<Right>", self.move_right)
        self.window.bind("<space>", self.shoot)

        # 게임이 window.mainloop() 실행되면 업데이트 함수 실행
        self.update_game()

    def move_left(self, event, distance: int = -20):
        '''왼쪽으로 distance 값 만큼 이동
            - event: self.window.bind("<Left>")에 등록된 왼쪽 방향키를 누른 경우
            - distance: 이동할 거리: 음(-)의 방향으로 20만큼
        '''
        self.canvas.move(self.player, distance, 0)

    def move_right(self, event, distance: int = 20):
        '''오른쪽쪽으로 distance 값 만큼 이동
            - event: self.window.bind("<Right>")에 등록된 오른쪽 방향키를 누른 경우
            - distance: 이동할 거리: 양(+)의 방향으로 20만큼
        '''
        self.canvas.move(self.player, distance, 0)

    def shoot(self, event, color='yellow'):
        '''총알 발사 함수'''
        # 플레이어 현재 좌표 추출
        x1, y1, x2, y2 = self.canvas.coords(self.player)
        # 추출된 좌표를 참고하여 총알 생성
        bullet = self.canvas.create_rectangle(x1+15, y1-10, x2-15, y1, fill=color)
        # __init__ 함수에서 생성한 총알 리스트에 등록
        self.bullets.append(bullet)

    def update_game(self, interval: int = 50):
        '''게임 상황을 업데이트'''
        self.move_bullets() # 총알 이동
        self.create_enemy() # 적 생성
        self.move_enemies() # 적 이동
        self.check_collisions() # 충돌 확인
        # 일정 시간이 지나면 업데이트를 반복적으로 수행
        self.window.after(
            ms=interval, # 시간 간격 설정: 50 밀리초(0.05초) 이후에 실행
            func=self.update_game # ms 이후에 실행할 함수 이름
        )

    def move_bullets(self):
        '''총알 이동'''
        for bullet in self.bullets:
            # 현재 등록된 총알이 있다면 이동
            self.canvas.move(bullet, 0, -10) # x축으로 0 픽셀, y축으로 -10 픽셀 이동
            # 총알이 이동하다가 화면 밖으로 나갔는지 확인
            if self.canvas.coords(bullet)[1] < 0: # 만약 총알 y값이 0보다 작다면
                self.canvas.delete(bullet)  # 화면 영역에서 객체 삭제
                self.bullets.remove(bullet) # 총알 리스트에서 객체 삭제

    def create_enemy(self, probability=0.05, size=20, color='red'):
        '''적 객체 생성
        - Args:
            - probability (float): 매 업데이트 시간에 적이 생성될 확률, 기본값 0.05 (5%)
            - size (int): 적의 크기, 기본값: 가로 20, 세로 20 픽셀
            - color (str): 적(enemy) 색깔
        '''
        rand_prob = random.random()
        if  rand_prob < probability:
            x_position = random.randint(0, self.width - size)
            # 객체의 좌측 상단 좌표: x0, y0
            x0, y0 = x_position, 0
            # 객체의 우측 하단 좌표: x1, y1
            x1, y1 = x_position+size, size
            enemy = self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)
            self.enemies.append(enemy)

    def move_enemies(self, distance=5):
        '''적 객체 이동'''
        for enemy in self.enemies:
            self.canvas.move(
                enemy, # 캔버스 내에서 이동할 객체 이름
                0, # 이동할 객체의 좌측 상단 x좌표로부터 이동할 값(픽셀)
                distance, # 이동할 객체의 좌측 상단 y좌표로부터 이동할 값(픽셀)
            )
            # 적이 캔버스 밖으로 나갔는지 확인
            # canvas.coords(객체이름)
            #   -> x0, y0, x1, y1
            # 객체 좌측상단: (x0, x1), 우측하단: (x1, y1)
            if self.canvas.coords(enemy)[3] > 600: # y1 좌표값 확인
                self.canvas.delete(enemy) # 캔버스에서 객체 삭제
                self.enemies.remove(enemy) # 리스트에서 객체 삭제

    def check_collisions(self):
        '''총알과 적 충돌 확인'''
        for bullet in self.bullets:
            bullet_coords = self.canvas.coords(bullet)
            for enemy in self.enemies:
                enemy_coords = self.canvas.coords(enemy)
                # 총알과 적이 충돌했을 경우 처리
                if self.overlap(bullet_coords, enemy_coords):
                    self.canvas.delete(bullet)  # 캔버스에서 총알 삭제
                    self.canvas.delete(enemy)   # 캔버스에서 적 삭제
                    self.bullets.remove(bullet) # 총알 리스트에서 해당 총알 삭제
                    self.enemies.remove(enemy)  # 적 리스트에서 해당 적 삭제
                    self.score += 1 # 점수 업데이트(맞추면 1점 추가)
                    break
    def overlap(self, coords1: tuple, coords2: tuple):
        '''2개 객체 좌표를 이용해 중첩 여부 확인
        - Args:
            - coords1 (tuple): x0, y0, x1, y1 (첫번째(총알) 객체의 좌측상단, 우측하단 좌표)
            - coords1 (tuple): x0, y0, x1, y1 (두번째(적)   객체의 좌측상단, 우측하단 좌표)
        '''
        if (coords1[0] < coords2[2] and
            coords1[2] > coords2[0] and
            coords1[1] < coords2[3] and
            coords1[3] > coords2[1]):
            return True
        return False

if __name__ == "__main__":
    game = ShootingGame()
    game.window.mainloop()