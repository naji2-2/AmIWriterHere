# 시작 화면
import tkinter as tk

class StartScreen(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.grid(row=0, column=0, sticky="nsew")

        label = tk.Label(self, text="시작 화면", font=("제주고딕", 20))
        label.pack(pady=15)


