import tkinter as tk
from PIL import Image, ImageTk
import re

class SelectRandomScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.grid(row=0, column=0, sticky="nsew")
        self.controller = controller

        # 등장인물, 키워드, 사건
        self.character = [0 for i in range(2)]
        self.keyword = ""
        self.incident = ""

        # 캔버스 생성
        self.canvas = tk.Canvas(self, width=2280, height=1800)
        self.canvas.grid(row=0, column=0, sticky="nsew")

        self.result_label = tk.Label(self, text="", font=("제주고딕", 25), fg="black", bg="white")
        self.result_label.place(x=60, y=300, anchor="nw")

        # 비눗방울 이미지
        bluebubble_image = Image.open("images/blue_bubble2.png")    # 이미지 경로
        resized_blue = bluebubble_image.resize((200, 200))          # 크기 조정
        bubblebutton_image = ImageTk.PhotoImage(resized_blue)
        # self.bb_image = ImageTk.PhotoImage(resized_blue)

        pinkbuble_image = Image.open("images/pink_bubble2.png")
        resized_pink = pinkbuble_image.resize((200, 200))
        pinkbuble_button = ImageTk.PhotoImage(resized_pink)

        orangebubble_image = Image.open("images/orange_bubble.png")
        resized_orange = orangebubble_image.resize((150, 150))
        self.bo_image = ImageTk.PhotoImage(resized_orange)

        greenbubble_image = Image.open("images/green_bubble.png")
        resized_green = greenbubble_image.resize((120, 120))
        self.bg_image = ImageTk.PhotoImage(resized_green)

        whitescreen_image = Image.open("images/White_Screen.png")
        resized_white = whitescreen_image.resize((1100, 650))
        self.ws_image = ImageTk.PhotoImage(resized_white)

        # 이미지를 캔버스에 추가
        #self.canvas.create_image(560, 25, image=self.bb_image, anchor="nw")
        self.canvas.create_image(880, 40, image=self.bo_image, anchor="nw")
        self.canvas.create_image(950, 90, image=self.bg_image, anchor="nw")
        self.canvas.create_image(60, 215, image=self.ws_image, anchor="nw")

        label = tk.Label(self, text="랜덤 소재 뽑기", font=("제주고딕", 100))
        label.place(relx=0.03, rely=0.05, anchor="nw")

        # 돌아가기 버튼
        back_button = tk.Button(self, text="← 돌아가기", font=("제주고딕", 25),
                                command=lambda: (controller.play_back_button_click_sound(), controller.show_frame("WritingScreen")))
        back_button.place(x=1180, y=100, anchor="nw")

        # 랜덤 주제 고르기 버튼
        random_button = tk.Button(self, image=pinkbuble_button, text="랜덤\n주제뽑기", font=("제주고딕", 25),
                                     compound="center",
                                     command=lambda: (controller.play_button_click_sound(), handle_random_selection()))
        random_button.image = pinkbuble_button
        random_button.place(x=1180, y=300, anchor="nw")

        # 글 쓰러 가기 버튼
        writingOk_button = tk.Button(self, image=bubblebutton_image,text="글 쓰기", font=("제주고딕", 25),
                                compound="center",
                                command=lambda: (controller.play_button_click_sound(), controller.show_frame("SelectRandomWritingScreen")))
        writingOk_button.image = bubblebutton_image     # 이미지 참조 유지
        writingOk_button.place(x=1180, y=600, anchor="nw")

        def handle_random_selection():
            # 랜덤 선택 함수 실행 후 결과 표시 함수 호출
            self.select_randoms()
            show_result()

        def show_result():
            self.result_label.config(
                text=f"\n   ▷ 캐릭터: {self.character[0], self.character[1]}  \n\n"
                     f"\n   ▷ 키워드: {self.keyword}  \n\n"
                     f"\n   ▷ 사건: {self.incident}  \n\n",
                font=("제주고딕", 40),
                justify="left",  # 왼쪽 정렬
                width=25,  # 가로너비 고정
                bg="white"  # 배경색 설정
            )
            self.result_label.place(x=60, y=300, anchor="nw")
            self.result_label.lift()  # 레이블 가장 위에 둠


    # 모든 랜덤 함수 실행, 값 저장
    def select_randoms(self):
        random = str(self.controller.new_random())
        # random의 특수 문자 없애기
        random = re.sub(r"[^\uAC00-\uD7A30-9a-zA-Z\s]", "", random)
        # 공백으로 문자열 나눠줌
        random = random.split(" ")
        self.character[0] = random[0]
        self.character[1] = random[1]
        print(self.character)
        self.keyword = random[2]
        self.incident = random[3]
        print("선택에서 실행")
        self.controller.character = self.character
        self.controller.keyword = self.keyword
        self.controller.incident = self.incident