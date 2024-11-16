import os
import tkinter as tk
from PIL import Image, ImageTk

class SelectRandomWritingScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.grid(row=0, column=0, sticky="nsew")
        self.controller = controller

        # controller에서 값 가져오기
        self.character = self.controller.character
        self.keyword = self.controller.keyword
        self.incident = self.controller.incident

        # 캔버스 생성
        self.canvas = tk.Canvas(self, width=2280, height=1800)
        self.canvas.grid(row=0, column=0, sticky="nsew")

        # 비눗방울 이미지
        bluebubble_image = Image.open("images/blue_bubble2.png")    # 이미지 경로
        resized_blue = bluebubble_image.resize((200, 200))          # 크기 조정
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
        # self.canvas.create_image(560, 25, image=self.bb_image, anchor="nw")
        self.canvas.create_image(1015, 40, image=self.bo_image, anchor="nw")
        self.canvas.create_image(1075, 90, image=self.bg_image, anchor="nw")
        # self.canvas.create_image(100, 30, image=self.gs_image, anchor="nw")
        self.canvas.create_image(60, 215, image=self.ws_image, anchor="nw")

        label = tk.Label(self, text="랜덤 주제 글 쓰기", font=("제주고딕", 100))
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

        # 제목에 특수 문자 저장을 위한 함수
        def replace_forbidden_chars(filename):
            replacements = {
                '?': '？',
                '*': '＊',
                '<': '＜',
                '>': '＞',
                ':': '：',
                '"': '＂',
                '/': '／',
                '\\': '＼',
                '|': '｜',
            }
            for forbidden, replacement in replacements.items():
                filename = filename.replace(forbidden, replacement)
            return filename

        def check_conditions_and_save():
            # controller에서 값 가져오기
            self.character = self.controller.character
            self.keyword = self.controller.keyword
            self.incident = self.controller.incident

            # 입력된 글 내용 가져오기
            text_content = self.writing_text.get("1.0", tk.END).strip()  # .strip() 텍스트에서 불필요한 개행 제거
            if not self.title:
                print("제목이 비어 있습니다!")
                return  # 제목이 없으면 저장하지 않음

            # 조건들에 맞지 않으면 저장하지 않음
            error_messages = []
            if self.character[0] not in text_content:
                error_messages.append(f"'{self.character[0]}'이/가 포함되지 않았습니다.\n")
            if self.character[1] not in text_content:
                error_messages.append(f"'{self.character[1]}'이/가 포함되지 않았습니다.\n")
            if self.keyword not in text_content:
                error_messages.append(f"'{self.keyword}'이/가 포함되지 않았습니다.\n")
            if self.incident not in text_content:
                error_messages.append(f"'{self.incident}'이/가 포함되지 않았습니다.")

            if error_messages:
                combined_message = "\n".join(error_messages)

                # 기존 레이블 삭제
                if hasattr(self, "error_label") and self.error_label is not None:
                    self.error_label.destroy()  # 레이블 삭제

                # 새로운 레이블 생성
                self.error_label = tk.Label(
                    self, text=combined_message, font=("제주고딕", 20), fg="red", bg="white", justify="left"
                )
                self.canvas.create_window(
                    300, 600, anchor="nw", window=self.error_label
                )
                return  # 조건이 맞지 않으면 함수 종료

            # 조건을 만족하는 경우에만 파일 저장 및 화면 전환
            save_folder = "C:/Users/USER/PycharmProjects/2024-Python-Project/user_novels/"

            # 금지된 문자 변환 후 파일 저장
            sanitized_title = replace_forbidden_chars(self.title)
            file_path = os.path.join(save_folder, f"{sanitized_title}.txt")

            try:
                # 파일 열기 및 내용 저장
                with open(file_path, "w", encoding="utf8") as Novel:
                    Novel.write(text_content)
                    Novel.close()
                print(f"'{file_path}'에 저장되었습니다.")
                clear_fields()

                # 조건을 만족하면 화면 전환
                controller.show_frame("StartScreen")  # 화면 전환

            except Exception as e:
                print(f"파일 저장 중 오류 발생: {e}")

        # 필드 비움
        def clear_fields():
            self.title_entry.delete(0, tk.END)
            self.writing_text.delete("1.0", tk.END)

        # 돌아가기 버튼
        back_button = tk.Button(self, text="← 돌아가기", font=("제주고딕", 25),
                                command=lambda: (clear_fields(), controller.play_back_button_click_sound(), controller.show_frame("SelectRandomScreen")))
        back_button.place(x=1180, y=50, anchor="nw")

        # 작성완료 버튼
        writingOk_button = tk.Button(self, image=bubblebutton_image, text="작성 완료", font=("제주고딕", 25),
                                      compound="center", command=lambda: (controller.play_button_click_sound(), check_conditions_and_save()))
        writingOk_button.image = bubblebutton_image     # 이미지 참조 유지
        writingOk_button.place(x=1180, y=600, anchor="nw")
