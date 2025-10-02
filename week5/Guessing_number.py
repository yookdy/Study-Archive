'''
게임에서 반복되는 상황의 루프를 만들어야 함
반복되는 기능을 함수를 클래스를 사용하여서 객체 지향을 사용함
'''
import tkinter as tk
from tkinter import messagebox 
import random

#init 함수를 만들고 self로 지정해주면 다른 함수에서 (self)라고 하고 사용할 수 있음
class NumberGuessingGame: 
    def __init__(self):     #객체 초기화 함수, 쓰는 
        self.window=tk.Tk()    #window 객체 생성
        self.window.geometry("500x300+500+500")
        self.window.title("숫자 맞추기 게임")
        #최대 최소의 범위를 설정해주는 변수를 만들어냄
        self.lower=1
        self.upper=100
        self.number_to_guess = random.randint(self.lower, self.upper)#범위 안에서의 랜덤값을 저장하는 변수
        self.num_guesses = 0 #입력환 횟수
        self.create_widgets() #위벳 메서드로 등록

    def create_widgets(self): #위젯 생성 메서드로 등록  
        #위젯의 디자인을 짜는 부분
        tk.Label(
            master=self.window, #해당하는 label이 속하는 파트를 정해줌
            text="숫자 맞추기 게임에 오신 것을 환영합니다!"
        ).pack(pady=20)
        tk.Label(
            master=self.window,
            text=f"{self.lower}과 {self.upper} 사이의 숫자를 맞춰보세요."
        ).pack(pady=20)
        self.entry = tk.Entry(master=self.window, justify='center')#텍스트 필드의 값을 입력받는 객체 
        self.entry.pack(pady=20)
        self.guess_button = tk.Button(
            master=self.window,
            text="Guess",
            command=self.check_guess #누르면 이 객체 안에 있는 check_guess 메서드가 실행됨 self의 역활
        )
        self.guess_button.pack(pady=20)
        self.result_label = tk.Label(master=self.window, text="") #결과를 출력하는 레이블
        self.result_label.pack()
    def check_guess(self):  #벡엔드 부분
        try:
            print(self.number_to_guess)#디버깅용 정답을 터미널에서 출력
            user_guess = int(self.entry.get()) #텍스트 필드에서의 값을 받는부분
            self.num_guesses += 1
            if user_guess < self.number_to_guess: 
                self.result_label.config(text="너무 낮아요!")
            elif user_guess > self.number_to_guess:
                self.result_label.config(text="너무 높아요!")
            else:
                self.result_label.config(
                    text=f"Congratulations! 정답 {self.num_guesses} 맞추셨습니다."
                )
                messagebox.showinfo(
                    "Game Over", f"{self.num_guesses}번 만에 맞췄습니다."
                )
                self.reset_game()#밑의 게임을 초기화화는 메서드 호출 
        except ValueError:
            self.result_label.config(text="입력 오류, 정수를 입력하세요 ^^.")

    def reset_game(self):       #게임을 초기화하는 메서드
        self.number_to_guess = random.randint(self.lower, self.upper)#랜덤값 초기화
        self.num_guesses =  0 #횟수 초기화
        self.entry.delete(0, tk.END)#텍스트 필드를 정리하는 역활을 함
        self.result_label.config(text="")#축하다는 말을 빈 공간으로 만들어냄

if __name__ == "__main__": #파일을 작동관련: 없어도 이 코드는 작동이 되지만 임포트 문제로 만들어냄 --------------------------------중요
#다른 파일을 모듈을 임포트해서 사용할 때 이 파일이 실행이 되는 것을 방지하기 위해서
    game = NumberGuessingGame()
    game.window.mainloop()