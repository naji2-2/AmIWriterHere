import tkinter as tk
from StartScreen import StartScreen

# 창 생성
window = tk.Tk()
window.title("이곳에선 내가 작가?!")

# 전체 화면 설정
window.attributes("-fullscreen", True)

# ESC 키를 눌러 전체 화면을 종료
def quit_fullscreen(event):
    window.attributes("-fullscreen", False)

window.bind("<Escape>", quit_fullscreen)

# 프레임 설정
container = tk.Frame(window)
container.pack(fill="both", expand=True)

# 화면 전환 함수
def show_frame(frame_class):
    frame = frame_class(container)
    frame.tkraise()

# 첫 화면 설정
show_frame(StartScreen)

# 창 실행
window.mainloop()