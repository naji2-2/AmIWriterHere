import tkinter as tk
from PIL import Image, ImageTk

class StartScreen(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.grid(row=0, column=0, sticky="nsew")

        # 캔버스 생성
        self.canvas = tk.Canvas(self, width=2280, height=1800)
        self.canvas.grid(row=0, column=0, sticky="nsew")

        # 비눗방울 이미지
        bluebubble_image = Image.open("images/blue_bubble.png") #이미지 걍로
        resized_blue = bluebubble_image.resize((360, 360))  #크기조정
        self.bb_image = ImageTk.PhotoImage(resized_blue)

        pinkbubble_image = Image.open("images/pink_bubble.png")
        resized_pink = pinkbubble_image.resize((350, 350))
        self.bp_image = ImageTk.PhotoImage(resized_pink)

        violetbubble_image = Image.open("images/violet_bubble.png")
        resized_violet = violetbubble_image.resize((250, 250))
        self.bv_image = ImageTk.PhotoImage(resized_violet)

        orangebubble_image = Image.open("images/orange_bubble.png")
        resized_orange = orangebubble_image.resize((150, 150))
        self.bo_image = ImageTk.PhotoImage(resized_orange)

        greenbubble_image = Image.open("images/green_bubble.png")
        resized_green = greenbubble_image.resize((350, 350))
        self.bg_image = ImageTk.PhotoImage(resized_green)

        # 이미지를 캔버스에 추가
        self.canvas.create_image(0, 0, image=self.bb_image, anchor="nw")
        self.canvas.create_image(950, 0, image=self.bp_image, anchor="nw")
        self.canvas.create_image(1200, 130, image=self.bv_image, anchor="nw")
        self.canvas.create_image(400, 700, image=self.bo_image, anchor="nw")
        self.canvas.create_image(100, 560, image=self.bg_image, anchor="nw")

        label = tk.Label(self, text="이곳에선 내가 작가?!", font=("제주고딕", 100))
        label.place(relx=0.5, rely=0.5, anchor="center")

        button_frame = tk.Frame(self)
        button_frame.place(x=1200, y=600, anchor="n")

        # 버튼 생성
        button_to_Writing = tk.Button(button_frame, text="글 쓰러가기 ▶", font=("제주고딕", 30))
        button_to_Reading = tk.Button(button_frame, text="글 보러가기 ▶", font=("제주고딕", 30))

        button_to_Writing.pack(side="top", padx=10, pady=15)
        button_to_Reading.pack(side="top", padx=10, pady=15)

