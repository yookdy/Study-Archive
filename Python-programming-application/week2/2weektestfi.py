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
