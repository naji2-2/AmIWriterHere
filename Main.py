import tkinter as tk

from StartScreen import StartScreen
from WritingScreen import WritingScreen
from FreeWritingScreen import FreeWritingScreen
from SelectRandomScreen import SelectRandomScreen
from SelectRandomWritingScreen import SelectRandomWritingScreen
import Random

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("이곳에선 내가 작가?!")
        self.geometry("2280x1080")
        self.attributes("-fullscreen", True)

        # 등장인물, 키워드, 사건
        self.character = []
        self.keyword = ""
        self.incident = ""

        # ESC 키를 눌러 전체 화면 종료
        self.bind("<Escape>", self.quit_fullscreen)

        # 프레임 컨테이너 설정
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # 화면 딕셔너리에 프레임 저장
        self.frames = {}

        for F in (StartScreen, WritingScreen, FreeWritingScreen, SelectRandomScreen, SelectRandomWritingScreen):
            page_name = F.__name__
            frame = F(container, self)  # controller로 self를 전달
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartScreen")  # 첫 화면을 StartScreen으로 설정

    def new_random(self):
        return Random.random_character(), Random.random_keyword(), Random.random_incident()

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def quit_fullscreen(self, event=None):
        self.attributes("-fullscreen", False)

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()