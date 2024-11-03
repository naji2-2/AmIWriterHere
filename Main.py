import tkinter as tk
from StartScreen import StartScreen

# 창 생성
window = tk.Tk()
window.title("이곳에선 내가 작가?!")
window.geometry("2280x1080")

# 전체 화면 설정
window.attributes("-fullscreen", True)

# ESC 키를 눌러 전체 화면을 종료
def quit_fullscreen(event):
    window.attributes("-fullscreen", False)

window.bind("<Escape>", quit_fullscreen)

# 프레임 설정
container = tk.Frame(window)
container.pack(fill="both", expand=True)
container.grid_rowconfigure(0, weight=1)
container.grid_columnconfigure(0, weight=1)

# 첫 화면 설정
start_screen = StartScreen(container)
start_screen.grid(row=0, column=0, sticky="nsew")
start_screen.tkraise()
# 창 실행
window.mainloop()