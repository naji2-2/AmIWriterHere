import os
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import scrolledtext


class ReadingScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.grid(row=0, column=0, sticky="nsew")
        self.controller = controller
        self.text_folder = "C:/Users/USER/PycharmProjects/2024-Python-Project/user_novels"  # 텍스트 파일이 저장된 폴더 경로
        self.file_name = ""
        self.file_path = ""

        # 캔버스 생성
        self.canvas = tk.Canvas(self, width=2280, height=1800)
        self.canvas.grid(row=0, column=0, sticky="nsew")

        # 비눗방울 이미지
        pinkbubble_image = Image.open("images/pink_bubble.png")     # 이미지 경로
        resized_pink = pinkbubble_image.resize((200, 200))          # 크기 조정
        self.bp_image = ImageTk.PhotoImage(resized_pink)

        violetbubble_image = Image.open("images/violet_bubble.png")
        resized_violet = violetbubble_image.resize((120, 120))
        self.bv_image = ImageTk.PhotoImage(resized_violet)

        whitescreen_image = Image.open("images/White_Screen.png")
        resized_white = whitescreen_image.resize((800, 600))
        self.ws_image = ImageTk.PhotoImage(resized_white)

        # 이미지를 캔버스에 추가
        self.canvas.create_image(450, 10, image=self.bp_image, anchor="nw")
        self.canvas.create_image(550, 90, image=self.bv_image, anchor="nw")
        self.canvas.create_image(500, 215, image=self.ws_image, anchor="nw")

        label = tk.Label(self, text="글 읽기", font=("제주고딕", 100))
        label.place(relx=0.03, rely=0.05, anchor="nw")

        # 파일 목록 표시
        self.file_list = tk.Listbox(self, font=("제주고딕", 25), selectmode=tk.SINGLE)
        self.file_list.place(x=50, y=215, width=400, height=600, anchor="nw")

        # 파일 로드 버튼
        load_button = tk.Button(self, text="파일 열기", font=("제주고딕", 25), command=self.view)
        load_button.place(x=150, y=820, anchor="nw")

        # 텍스트 내용 표시 영역
        self.text_area = scrolledtext.ScrolledText(self, wrap=tk.WORD, font=("제주고딕", 30))
        self.text_area.place(x=500, y=215, w=800, h=600, anchor="nw")
        self.text_area.configure(state="disabled")  # 읽기 전용으로 설정

        # 텍스트 폴더의 파일 목록을 로드
        self.load_file_list()

        # 주기적으로 파일 목록 갱신
        self.auto_refresh()

        # 돌아가기 버튼
        back_button = tk.Button(self, text="← 돌아가기", font=("제주고딕", 25),
                                command=lambda: controller.show_frame("StartScreen"))
        back_button.place(x=1180, y=50, anchor="nw")

    # 텍스트 파일 목록을 불러와 리스트에 추가
    def load_file_list(self):
        self.file_list.delete(0, tk.END)
        try:
            files = os.listdir(self.text_folder)
            for file in files:
                if file.endswith(".txt"):  # 텍스트 파일만 추가
                    self.file_list.insert(tk.END, file)
        except Exception as e:
            print(f"파일 목록을 불러오는 중 오류 발생: {str(e)}")

    def view(self):
        """선택된 파일의 내용을 텍스트 영역에 표시"""
        selected_index = self.file_list.curselection()
        if selected_index:
            self.file_name = self.file_list.get(selected_index)
            self.file_path = self.text_folder + "/" + self.file_name

            # 텍스트 영역 초기화 후 파일 내용 로드
            self.text_area.configure(state="normal")
            self.text_area.delete(1.0, tk.END)
            try:
                with open(self.file_path, "r", encoding="utf-8") as file:
                    content = file.read()
                    self.text_area.insert(tk.END, content)
            except Exception as e:
                self.text_area.insert(tk.END, f"파일을 열 수 없습니다: {str(e)}")
            self.text_area.configure(state="disabled")  # 읽기 전용으로 설정

        else:
            print("파일을 선택하지 않았습니다!")

    # 일정 시간마다 파일 목록을 갱신함
    def auto_refresh(self):
        self.load_file_list()
        self.after(3000, self.auto_refresh)  # 5초마다 실행