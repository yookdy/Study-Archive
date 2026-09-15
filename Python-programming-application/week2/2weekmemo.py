'''기본
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11] #x,y의 총 갯수는 같아야함
# 그래프 생성
plt.plot(x, y)
# 그래프에 제목과 축 레이블 추가
plt.title('Line Plot Example')
plt.xlabel('X Axis')=======================기본 x,y, 제목을 설정
plt.ylabel('Y Axis')
# 그래프 표시
plt.show()

'''

#---------막대--------
'''
import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D', 'E']
values = [10, 24, 36, 40, 5]
# 그래프 생성
plt.bar(categories, values)#막대 그래프 생성하는 것
# 그래프에 제목과 축 레이블 추가 akreo 막대바의 카테고리하고 값의 갯수가 같아야함
plt.title('Bar Chart Example')
plt.xlabel('Categories')
plt.ylabel('Values')
# 그래프 표시
plt.show()
'''

#----------히스토그램----------
'''
import matplotlib.pyplot as plt
# 데이터 준비
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 7, 8, 9]
# 히스토그램 그리기
plt.hist(data, bins=5, color='skyblue', edgecolor='black', alpha=0.7)디지인 하는 부분
# bins: 가로(x)축 구간 개수
# color: 색상 지정
# edgeclolor: 히스토그램 막대 테두리 색상
# alpha: 히스토그램 막대 투명도
# 그래프에 제목과 축 레이블 추가

plt.title('Colored Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')
# 그래프 표시
plt.show()

'''
#plt.scatter(x, y) 점으로 그래프 생성
# 이 안에 색이나 크기를 조정하는데 사용 가능함 plt.scatter(x=~,y=~,s=sizes,c=color))
#plt.pie 원으로 된 그래프를 생성하는 역활을 함
#--------------------multi plot-------------

import matplotlib.pyplot as plt
import numpy as np


#여러개의 그래프를 표현하는 방법---Mulit-plot
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
#--------->x동일하게 사용, y 즉 치역을 다르게 나타냄
# Figure와 Subplot 생성
ti, (ax1, ax2) = plt.subplots(2, 1)#행:2 열:1 fig는 내가 임의로 정한 객체의 이름
# 첫 번째 Subplot
ax1.plot(x, y1)
ax1.set_title('Sine Wave')
# 두 번째 Subplot
ax2.plot(x, y2)
ax2.set_title('Cosine Wave')
# 레이아웃 조정
plt.tight_layout()
# 그래프 표시
plt.show()

#---------------------
'''
import matplotlib.pyplot as plt
import numpy as np

# 데이터 생성
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
y4 = np.exp(-x)
# Figure와 Subplot 생성
fig, axs = plt.subplots(2, 2, figsize=(10,8))#페이지의 크기를 확인
# 첫 번째 Subplot: 0번째 행, 0번째 열
axs[0, 0].plot(x, y1)
axs[0, 0].set_title('Sine Wave')
# 두 번째 Subplot: 0번째 행, 1번째 열
axs[0, 1].plot(x, y2)
axs[0, 1].set_title('Cosine Wave')
# 세 번째 Subplot: 1번째 행, 0번째 열
axs[1, 0].plot(x, y3)
axs[1, 0].set_title('Tangent Wave')
# 네 번째 Subplot: 1번째 행, 1번째 열
axs[1, 1].plot(x, y4)
axs[1, 1].set_title('Exponential Decay')
# 레이아웃 조정
'''
#---------------Funcanimation-------
'''
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
# 데이터 생성 함수
def update(frame):
    # 업데이트할 데이터
     line.set_ydata(np.sin(x + frame / 10.0)) 
     return line,
# 초기화 함수
def init():
    line.set_ydata(np.ma.array(x, mask=True))
    return line,
# 데이터 준비
x = np.linspace(0, 2 * np.pi, 100)
fig, ax = plt.subplots()
line, = ax.plot(x, np.sin(x))#전역변수
# 애니메이션 생성
ani = animation.FuncAnimation(
    fig,#그림을 생성하는 거
    update,#시간을 지속적으로 업데이트하는거
    frames=100,
    init_func=init,
    blit=True
)
# 화면에 플롯 시현
plt.show()

'''

#----------artistanimation---------
#위와 다르게 실시간으로 움직이기에 업데이트가 필요없음
'''
mport numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
fig, ax = plt.subplots()

# 저장된 데이터를 불러왔다고 가정
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)
artists = []
for i in range(len(x)):
     point, = ax.plot(x[i], y[i], 'ro')
     artists.append([point])
ani = animation.ArtistAnimation(
	fig, artists, interval=50, blit=True
)
plt.show()
'''

#계산기 만들기
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