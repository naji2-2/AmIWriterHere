import pygame
import tkinter as tk
from ReadingScreen import ReadingScreen
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

        # 배경 음악 및 효과음 초기화
        pygame.mixer.init()         # pygame 오디오 초기화
        self.background_music = "music/background_music.mp3"    # 배경 음악 경로
        self.button_click_sound = "music/button_click_sound.mp3"    # 버튼 클릭 효과음 경로
        self.back_button_click_sound = "music/back_button_click_sound.mp3"  # 버튼 클릭 효과음 경로
        self.play_background_music()

        # 등장인물, 키워드, 사건
        self.character = []
        self.keyword = ""
        self.incident = ""

        # 파일이름, 정보
        self.file_name = ""
        self.file_path = ""

        # ESC 키를 눌러 전체 화면 종료
        self.bind("<Escape>", self.quit_fullscreen)

        # 프레임 컨테이너 설정
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # 화면 딕셔너리에 프레임 저장
        self.frames = {}

        for F in (StartScreen, WritingScreen, FreeWritingScreen, SelectRandomScreen, SelectRandomWritingScreen, ReadingScreen):
            page_name = F.__name__
            frame = F(container, self)  # controller로 self를 전달
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartScreen")  # 첫 화면을 StartScreen으로 설정

    # 배경음악 재생
    def play_background_music(self):
        pygame.mixer.music.load(self.background_music)
        pygame.mixer.music.play(loops=-1)  # 무한 반복

    # 버튼 클릭 효과음
    def play_button_click_sound(self):
        click_sound = pygame.mixer.Sound(self.button_click_sound)
        #click_sound.set_volume(0.5)
        click_sound.play()

    # 돌아가기 버튼 클릭 효과음
    def play_back_button_click_sound(self):
        click_sound = pygame.mixer.Sound(self.back_button_click_sound)
        click_sound.play()

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