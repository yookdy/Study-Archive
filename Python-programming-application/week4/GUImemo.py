#메뉴를 만들기
#패키지를 가져옴
#기본적이 메모장을 만들----파일에서 중복 확인 저장 확인 하는 기능은 없음


#기본적인 기능을 넣고 찾기 기능 추가


import tkinter as tk
from tkinter import messagebox, filedialog

window=tk.Tk()#객체 생성
window.title("메모장")
window.geometry("500x300+200+200")
menu=tk.Menu(window)#메뉴 객체 생성--Menu는 클래스
window.config(menu=menu)#메뉴를 윈도우에 설정, 원도우만 가능함


def new_file():
    text_area.delete(1.0, tk.END)#텍스트 필드의 내용을 line1에서 끝까지 지우기

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path: #파일 경로가 존재할 때
        with open(file_path, "r", encoding="utf8") as file:#선택된 파일을 읽기 모드로 열기 임의로 file이라는 변수를 만듬
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, file.read())#임시 파일을 넣는거
            #파일을 열어서 텍스트 필드에 내용을 삽입


def save_file():#경로 파일이 필요함
    file_path = filedialog.asksaveasfilename(
        defaultextenion=".txt",
        filetypes=[("텍스트 파일", "*.txt"), ("모든 파일", "*.*")]
    )
    if file_path:
        with open(file_path, 'w', encoding="utf8") as file:     #open(경로, 모드, 인코딩)
            file.write(text_area.get(1.0, tk.END))#get을 이용해서 텍스트 필드의 내용을 가져옴 
        messagebox.showinfo("저장 완료", f"파일이 저장되었습니다: {file_path}")

# file_path = filedialog.askopenfilename()
# file_path = filedialog.asksaveasfilename()
#------->파일 대화상자를 여는 코드


# 상단에 툴바 프레임 생성 없으면 왼쪽에 프레임이 생성됨
toolbar = tk.Frame(window)
toolbar.pack(side="top", fill="x")

# "파일" 메뉴버튼
file_btn = tk.Menubutton(toolbar, text="파일", relief="raised")
file_menu = tk.Menu(file_btn, tearoff=0)#파일을 누르면 밑에 내용이 나오게 만듬

#command는 함수를 호출하게 하는 부분
file_menu.add_command(label="열기", command=open_file)
file_menu.add_command(label="저장", command=save_file)
file_menu.add_command(label="새 파일", command=new_file)
file_menu.add_separator()
file_menu.add_command(label="종료", command=window.quit)#.qui는 윈도우 객체를 종료하는 역활
file_btn.config(menu=file_menu)
file_btn.pack(side="left")#패딩으로 생각하기

# "도움말" 메뉴버튼
help_btn = tk.Menubutton(toolbar, text="도움말", relief="raised")
help_menu = tk.Menu(help_btn, tearoff=0)
help_menu.add_command(
    label="정보",
    command=lambda: messagebox.showinfo("정보", "Tkinter 고급 기능 예제")
)
help_btn.config(menu=help_menu)
help_btn.pack(side="left")
# 상태 표시줄 추가하기 위한 레이블 객체 생성
status = tk.Label(
    window, # 상태 표시줄을 등록할 객체 
    text="상태: 대기 중", 
    bd=1, # 경계선 굵기
    relief=tk.SUNKEN, # 상태 표시줄 표시 방법, 
    # SUNKEN: 움푹 들어간 형태, 
    # FLAT: 다른 객체와 동일, 
    # RAISED: 돌출된 모양, 
    # GROOVE: 테두리 모양으로 구분
    anchor=tk.W # west(왼쪽) 정렬
)
status.pack(
    side=tk.BOTTOM, # 객체 위치 
    # BOTTOM: 바닥에 배치, 
    # TOP: 상단 배치, 
    # LEFT: 왼쪽 배치, 
    # RIGHT: 오른쪽 배치
    fill=tk.X, 
    # fill: 사용되지 않는 공간으로 늘이기
    #fill=tk.(아래거)
    # X: X축으로 가득 채우기(수평으로만 늘이기)
    # Y: Y축으로 가득 채우기(수직으로만 늘이기)
    # BOTH: 가능한 모든 공간으로 늘이기
    # NONE: 늘이지 않기 (원래 크기 유지)
    
)#패딩의 구체덕인 역활을 넣음
# 버튼 추가
text_area=tk.Text(window)#윈도우에 텍스트 영역 생성
text_area.pack(expand=1, fill=tk.BOTH)
# 메인 루프 실행
window.mainloop()

