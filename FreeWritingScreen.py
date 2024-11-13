import os
import tkinter as tk
from PIL import Image, ImageTk

class FreeWritingScreen(tk.Frame):
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

        pinkbubble_image = Image.open("images/pink_bubble.png")
        resized_pink = pinkbubble_image.resize((200, 200))
        self.bp_image = ImageTk.PhotoImage(resized_pink)

        violetbubble_image = Image.open("images/violet_bubble.png")
        resized_violet = violetbubble_image.resize((120, 120))
        self.bv_image = ImageTk.PhotoImage(resized_violet)

        grayscreen_image = Image.open("images/Gray_Screen.png")
        resized_gray = grayscreen_image.resize((200, 200))
        self.gs_image = ImageTk.PhotoImage(resized_gray)

        whitescreen_image = Image.open("images/White_Screen.png")
        resized_white = whitescreen_image.resize((1100, 650))
        self.ws_image = ImageTk.PhotoImage(resized_white)

        # 이미지를 캔버스에 추가
        #self.canvas.create_image(560, 25, image=self.bb_image, anchor="nw")
        self.canvas.create_image(710, 10, image=self.bp_image, anchor="nw")
        self.canvas.create_image(810, 90, image=self.bv_image, anchor="nw")
        #self.canvas.create_image(100, 30, image=self.gs_image, anchor="nw")
        self.canvas.create_image(60, 215, image=self.ws_image, anchor="nw")

        label = tk.Label(self, text="자유 글 쓰기", font=("제주고딕", 100))
        label.place(relx=0.03, rely=0.05, anchor="nw")

        title_label = tk.Label(self, text="제목 : ", font=("제주고딕", 25), bg="white")
        title_label.place(x=100, y=230, anchor="nw")

        # 제목 입력 받기
        self.title_entry = tk.Entry(self, font=("제주고딕", 20), width=30)
        self.title_entry.place(x=200, y=230, anchor="nw")

        # 포커스 아웃 이벤트 핸들러
        def on_focus_out(event):
            self.title = self.title_entry.get()
            print(f"입력된 제목: {self.title}")

        # Entry에 포커스 아웃 이벤트 바인딩
        self.title_entry.bind("<FocusOut>", on_focus_out)

        # 글 입력 받기
        self.writing_text = tk.Text(self, font=("제주고딕", 20), bg="white")
        self.writing_text.place(x=100, y=300, w=1000, h=550, anchor="nw")

        def display_input():
            if not self.title:
                print("제목이 비어 있습니다!")
                return  # 제목이 없으면 저장하지 않음

            # 사용자가 지정한 제목으로 파일 만들기
            save_folder = "C:/Users/USER/PycharmProjects/2024-Python-Project/user_novels/"

            # 파일 경로 생성
            file_path = os.path.join(save_folder, f"{self.title}.txt")

            try:
                # 파일 열기 및 내용 저장
                with open(file_path, "w", encoding="utf8") as Novel:
                    Novel.write(self.writing_text.get("1.0", tk.END).strip())
                print(f"'{file_path}'에 저장되었습니다.")
            except Exception as e:
                print(f"파일 저장 중 오류 발생: {e}")

        # 돌아가기 버튼
        back_button = tk.Button(self, text="← 돌아가기", font=("제주고딕", 25),
                                command=lambda: controller.show_frame("WritingScreen"))
        back_button.place(x=1180, y=50, anchor="nw")

        # 작성완료 버튼
        writingOk_button = tk.Button(self, image=bubblebutton_image, text="작성 완료", font=("제주고딕", 25),
                                     compound="center",
                                     command=lambda: (display_input(), controller.show_frame("StartScreen")))
        writingOk_button.image = bubblebutton_image     # 이미지 참조 유지
        writingOk_button.place(x=1180, y=600, anchor="nw")