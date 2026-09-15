import tkinter as tk

# 버튼 클릭 시 동작을 정의하는 함수
# 숫자 버튼을 클릭했을 때
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))
# "Clear" 버튼을 클릭했을 때
def button_clear():
    entry.delete(0, tk.END)
# "=" 버튼을 클릭했을 때
def button_equal():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

#--------------------------------------------
# 메인 윈도우 생성
window = tk.Tk()
window.title("계산기")
# 텍스트 입력 필드 추가
entry = tk.Entry(window, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
# 버튼 추가
button_1 = tk.Button(window, text="1", padx=20, pady=20, command=lambda: button_click(1))
button_2 = tk.Button(window, text="2", padx=20, pady=20, command=lambda: button_click(2))
button_3 = tk.Button(window, text="3", padx=20, pady=20, command=lambda: button_click(3))
button_4 = tk.Button(window, text="4", padx=20, pady=20, command=lambda: button_click(4))
button_5 = tk.Button(window, text="5", padx=20, pady=20, command=lambda: button_click(5))
button_6 = tk.Button(window, text="6", padx=20, pady=20, command=lambda: button_click(6))
button_7 = tk.Button(window, text="7", padx=20, pady=20, command=lambda: button_click(7))
button_8 = tk.Button(window, text="8", padx=20, pady=20, command=lambda: button_click(8))
button_9 = tk.Button(window, text="9", padx=20, pady=20, command=lambda: button_click(9))
button_0 = tk.Button(window, text="0", padx=20, pady=20, command=lambda: button_click(0))
button_add = tk.Button(window, text="+", padx=20, pady=20, command=lambda: button_click("+"))
button_equal = tk.Button(window, text="=", padx=20, pady=20, command=button_equal)
button_clear = tk.Button(window, text="Clear", padx=20, pady=20, command=button_clear)

# 버튼을 그리드에 배치--------------------------------------위치를 맞춰줌
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1)
button_clear.grid(row=5, column=2)
# 메인 루프 실행
window.mainloop()


