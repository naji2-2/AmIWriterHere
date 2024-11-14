import os
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import scrolledtext

class ReadingScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.grid(row=0, column=0, sticky="nsew")
        self.controller = controller

        # 텍스트 파일 경로 설정
        self.text_folder = "C:/Users/USER/PycharmProjects/2024-Python-Project/user_novels"

        # 캔버스 생성
        self.canvas = tk.Canvas(self, width=2280, height=1800)
        self.canvas.grid(row=0, column=0, sticky="nsew")

        # 비눗방울 이미지
        bluebubble_image = Image.open("images/blue_bubble2.png")    # 이미지 경로
        resized_blue = bluebubble_image.resize((200, 200))          # 크기 조정
        bubblebutton_image = ImageTk.PhotoImage(resized_blue)

        pinkbubble_image = Image.open("images/pink_bubble.png")
        resized_pink = pinkbubble_image.resize((200, 200))
        self.bp_image = ImageTk.PhotoImage(resized_pink)

        violetbubble_image = Image.open("images/violet_bubble.png")
        resized_violet = violetbubble_image.resize((120, 120))
        self.bv_image = ImageTk.PhotoImage(resized_violet)

        orangebubble_image = Image.open("images/orange_bubble.png")
        resized_orange = orangebubble_image.resize((150, 150))
        self.bo_image = ImageTk.PhotoImage(resized_orange)

        greenbubble_image = Image.open("images/green_bubble.png")
        resized_green = greenbubble_image.resize((350, 350))
        self.bg_image = ImageTk.PhotoImage(resized_green)

        whitescreen_image = Image.open("images/White_Screen.png")
        resized_white = whitescreen_image.resize((1100, 650))
        self.ws_image = ImageTk.PhotoImage(resized_white)

        # 이미지를 캔버스에 추가
        self.canvas.create_image(450, 10, image=self.bp_image, anchor="nw")
        self.canvas.create_image(550, 90, image=self.bv_image, anchor="nw")
        self.canvas.create_image(300, 700, image=self.bo_image, anchor="nw")
        self.canvas.create_image(20, 560, image=self.bg_image, anchor="nw")
        self.canvas.create_image(60, 215, image=self.ws_image, anchor="nw")

        label = tk.Label(self, text="글 보기", font=("제주고딕", 100))
        label.place(relx=0.03, rely=0.05, anchor="nw")

        button_frame = tk.Frame(self)
        button_frame.place(x=1200, y=600, anchor="n")

        # 텍스트 파일 목록 표시 프레임
        file_list_frame = tk.Frame(self)
        file_list_frame.place(x=60, y=215, w=1100, h=650)

        self.file_list = tk.Listbox(file_list_frame, font=("제주고딕", 30))
        self.file_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # 텍스트 파일 목록 스크롤바
        scrollbar = tk.Scrollbar(file_list_frame, orient=tk.VERTICAL, command=self.file_list.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.file_list.config(yscrollcommand=scrollbar.set)

        # 텍스트 파일 목록 초기화
        self.load_text_files()

        # 돌아가기 버튼
        back_button = tk.Button(self, text="← 돌아가기", font=("제주고딕", 25),
                                command=lambda: controller.show_frame("StartScreen"))
        back_button.place(x=1180, y=50, anchor="nw")

        # 글 읽기 버튼
        reading_button = tk.Button(self, image=bubblebutton_image, text="읽기", font=("제주고딕", 25),
                                     compound="center")
        reading_button.image = bubblebutton_image  # 이미지 참조 유지
        reading_button.place(x=1180, y=600, anchor="nw")

    def load_text_files(self):
        # 폴더에서 텍스트 파일 목록을 불러와 리스트에 추가
        if os.path.exists(self.text_folder):
            for file_name in os.listdir(self.text_folder):
                if file_name.endswith(".txt"):  # 텍스트 파일만 추가
                    self.file_list.insert(tk.END, file_name)

