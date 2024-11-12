import tkinter as tk
from PIL import Image, ImageTk

class SelectRandomScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.grid(row=0, column=0, sticky="nsew")
        self.controller = controller

        # 캔버스 생성
        self.canvas = tk.Canvas(self, width=2280, height=1800)
        self.canvas.grid(row=0, column=0, sticky="nsew")

        # 비눗방울 이미지
        bluebubble_image = Image.open("images/blue_bubble2.png")  # 이미지 걍로
        resized_blue = bluebubble_image.resize((200, 200))  # 크기조정
        bubblebutton_image = ImageTk.PhotoImage(resized_blue)
        # self.bb_image = ImageTk.PhotoImage(resized_blue)

        orangebubble_image = Image.open("images/orange_bubble.png")
        resized_orange = orangebubble_image.resize((150, 150))
        self.bo_image = ImageTk.PhotoImage(resized_orange)

        greenbubble_image = Image.open("images/green_bubble.png")
        resized_green = greenbubble_image.resize((120, 120))
        self.bg_image = ImageTk.PhotoImage(resized_green)

        grayscreen_image = Image.open("images/Gray_Screen.png")
        resized_gray = grayscreen_image.resize((200, 200))
        self.gs_image = ImageTk.PhotoImage(resized_gray)

        whitescreen_image = Image.open("images/White_Screen.png")
        resized_white = whitescreen_image.resize((1100, 650))
        self.ws_image = ImageTk.PhotoImage(resized_white)

        # 이미지를 캔버스에 추가
        #self.canvas.create_image(560, 25, image=self.bb_image, anchor="nw")
        self.canvas.create_image(880, 40, image=self.bo_image, anchor="nw")
        self.canvas.create_image(950, 90, image=self.bg_image, anchor="nw")
        #self.canvas.create_image(100, 30, image=self.gs_image, anchor="nw")
        self.canvas.create_image(60, 215, image=self.ws_image, anchor="nw")

        label = tk.Label(self, text="랜덤 소재 뽑기", font=("제주고딕", 100))
        label.place(relx=0.03, rely=0.05, anchor="nw")

        # 돌아가기 버튼
        back_button = tk.Button(self, text="← 돌아가기", font=("제주고딕", 25),
                                command=lambda: controller.show_frame("WritingScreen"))
        back_button.place(x=1180, y=50, anchor="nw")

        # 글 쓰러 가기 버튼
        writingOk_button = tk.Button(self, image=bubblebutton_image,text="글 쓰기", font=("제주고딕", 25),
                                compound="center",
                                command=lambda: controller.show_frame("SelectRandomWritingScreen"))
        writingOk_button.image = bubblebutton_image     # 이미지 참조 유지
        writingOk_button.place(x=1180, y=600, anchor="nw")