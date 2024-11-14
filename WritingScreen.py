import tkinter as tk
from PIL import Image, ImageTk

class WritingScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # 캔버스 생성
        self.canvas = tk.Canvas(self, width=2280, height=1800)
        self.canvas.grid(row=0, column=0, sticky="nsew")

        # 비눗방울 이미지
        bluebubble_image = Image.open("images/blue_bubble2.png")    # 이미지 경로
        resized_blue = bluebubble_image.resize((350, 350))          # 크기 조정
        self.bb_image = ImageTk.PhotoImage(resized_blue)

        pinkbubble_image = Image.open("images/pink_bubble.png")
        resized_pink = pinkbubble_image.resize((200, 200))
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
        self.canvas.create_image(560, 25, image=self.bb_image, anchor="nw")
        self.canvas.create_image(920, 10, image=self.bp_image, anchor="nw")
        self.canvas.create_image(930, 200, image=self.bv_image, anchor="nw")
        self.canvas.create_image(350, 700, image=self.bo_image, anchor="nw")
        self.canvas.create_image(50, 560, image=self.bg_image, anchor="nw")

        label = tk.Label(self, text="글 쓰기", font=("제주고딕", 100))
        label.place(relx=0.03, rely=0.05, anchor="nw")

        # 주제 리스트
        topic_options = ["로멘스 판타지", "스릴러", "코미디", "로맨스", "판타지", "액션", "미스터리"]
        self.selected_option = tk.StringVar(value="주제 선택")  #기본값 설정

        # 주제가 선택될 때마다 show_selected_option 메서드 호출
        self.selected_option.trace("w", lambda *args: self.show_selected_option())

        # 드롭 다운
        dropdown_topic = tk.OptionMenu(self, self.selected_option, *topic_options)
        dropdown_topic.config(font=("제주고딕", 30))
        dropdown_topic.place(x=80, y=250, anchor="nw")
        #dropdown_topic.pack(pady=20)

        button_frame = tk.Frame(self)
        button_frame.place(x=1200, y=600, anchor="n")

        # 버튼 생성
        button_to_Free = tk.Button(button_frame, text="자유 글 쓰기 ▶", font=("제주고딕", 30),
                                      command=lambda: controller.show_frame("FreeWritingScreen"))
        button_to_Random = tk.Button(button_frame, text="랜덤 소재 뽑기 ▶", font=("제주고딕", 30),
                                     command=lambda: controller.show_frame("SelectRandomScreen"))

        button_to_Free.pack(side="top", padx=10, pady=15)
        button_to_Random.pack(side="top", padx=10, pady=15)

        # 돌아가기 버튼
        back_button = tk.Button(self, text="← 돌아가기", font=("제주고딕", 25),
                                command=lambda: controller.show_frame("StartScreen"))
        back_button.place(x=1180, y=50, anchor="nw")

    # 선택 된 주제
    def show_selected_option(self):
        selected = self.selected_option.get()
        print(f"선택된 옵션: {selected}")