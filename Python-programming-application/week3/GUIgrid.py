import tkinter as tk #외부 라이브러리를 가져옴

win = tk.Tk() #원도우 객체 생성
win.title('cju python')#
for i in range(5):
    for j in range(3):  #이중 배열을 사용하기
        frame = tk.Frame(
        master = win,
        relief = tk.RAISED, # 디자인에서 사용되는 코드 경계 안쪽이 바깥보다 볼록하게 보임
        borderwidth = 1     #1픽셀을 테두리로 잡은 상태 # 참고: https://opentutorials.org/module/3181/18805 
        )
        frame.grid(row=i, column=j)#2차원 배열을 생성하는 디자인을 하는데 사용하기
        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack()
win.mainloop()