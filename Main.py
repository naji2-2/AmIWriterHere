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

        self.character = Random.random_character()
        print("등장인물 : {0}, {1}".format(self.character[0], self.character[1]))
        self.keyword = Random.random_keyword()
        print("키워드 : {}".format(self.keyword))
        self.incident = Random.random_incident()
        print("사건 : {}".format(self.incident))

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
            # SelectRandomScreen과 SelectRandomWritingScreen을 제외한 클래스는 기본적으로 인자 없이 생성
            if F in (SelectRandomScreen, SelectRandomWritingScreen):
                frame = F(container, self, self.character, self.keyword, self.incident)
            else:
                frame = F(container, self)  # 다른 화면은 기본적으로 self만 전달
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartScreen")  # 첫 화면을 StartScreen으로 설정

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def quit_fullscreen(self, event=None):
        self.attributes("-fullscreen", False)

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()