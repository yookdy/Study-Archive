'''
기본적인 틀 
import tkinter as tk
# 윈도우 객체 생성
window = tk.Tk()
# 메인 루프 실행
window.mainloop()
'''


# pack( ): 윈도우, 프레임 내에서 위젯의 순서를 할당
# grid( ): 격자를 생성하여 위젯을 순서대로 할당
# place( ): 프로그래머가 위젯 위치를 명시적으로 지정

'''
3곱하기 5격자를 만들기
import tkinter as tk

win = tk.Tk() #원도우 객체 생성
win.title('cju python')
for i in range(5):
    for j in range(3):  #이중 배열을 사용하기
        frame = tk.Frame(
        master = win,
        relief = tk.RAISED, # 경계 안쪽이 바깥보다 볼록하게 보임
        borderwidth = 1     # 참고: https://opentutorials.org/module/3181/18805 
        )
        frame.grid(row=i, column=j)#디자인을 하는데 사용하기
        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack()
win.mainloop()
'''

'''
#위에 top이라고 하는 창을 넣고 밑에 코드를 실행하는 역활을 함
from tkinter import *

# 윈도우 객체 생성 및 크기 지정
top = Tk()
top.geometry("400x250")

# Label (글자) 객체 생성
Username = Label(top, text = "Username").place(x = 30,y = 50)#텍스트하고 위치를 설정해줌
email = Label(top, text = "Email").place(x = 30, y = 90)
password = Label(top, text = "Password").place(x = 30, y = 130)

# Entry (입력) 객체를 생성하고 위치를 직접 지정
e1 = Entry(top).place(x = 80, y = 50)
e2 = Entry(top).place(x = 80, y = 90)
e3 = Entry(top).place(x = 95, y = 130)
# 메인 루푸 실행
top.mainloop()
'''

#페딩을 이용해서 코드를 사용하는 역활을 함
'''
import tkinter as tk
# 메인 윈도우 생성

window = tk.Tk()
window.title("Tkinter 기본 앱")
window.geometry('500x300+200+200')
# 레이블 추가 및 위치 지정
label = tk.Label(window, text="Hello, Tkinter!")
label.pack(padx=10, pady=10) # pack() 메서드 사용, 패딩 추가
# 텍스트 입력 필드 추가
entry = tk.Entry(window)
entry.pack(padx=10, pady=10) # pack() 메서드 사용, 패딩 추가
# 메인 루프 실행
window.mainloop()
'''

#버튼 기능
"""
import tkinter as tk

ment="dkdkdkdk"
# 메인 윈도우 생성
window = tk.Tk()
window.title("Tkinter 기본 앱")
window.geometry('500x300+200+200')

# 레이블 추가 및 위치 지정
label = tk.Label(window, text=ment)
label.pack(padx=10, pady=10) # pack() 메서드 사용, 패딩 추가

# 텍스트 입력 필드 추가
entry = tk.Entry(window)
entry.pack(padx=10, pady=10) # pack() 메서드 사용, 패딩 추가

# 버튼이 클릭되었을 때 수행할 작업 정의
def on_button_click():
    '''모니터에 입력 내용을 간단히 출력하여 작동 여부 확인'''
    print(f"버튼이 클릭되었습니다! 입력 내용:{entry.get()}")

# 버튼 추가
button = tk.Button(window, text="Click Me!", command=on_button_click)
button.pack(padx=10, pady=10) # pack() 메서드 사용, 패딩 추가


# 체크박스 추가
checkbox_var = tk.BooleanVar()#불리안 바
checkbox = tk.Checkbutton(window, text="Check me", variable=checkbox_var)
checkbox.pack(padx=10, pady=10) # pack() 메서드 사용, 패딩 추가

# 메인 루프 실행
window.mainloop()

#------------> 터미널에 출력이 됨
"""