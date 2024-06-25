import tkinter as tk
from datetime import datetime

class ChatBotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("チャットボット")
        self.root.geometry("500x400")  # ウィンドウのサイズを設定

        self.chat_log = tk.Text(self.root, state='disabled', width=50, height=20)
        self.chat_log.grid(row=0, column=0, columnspan=2)

        self.msg_entry = tk.Entry(self.root, width=50)
        self.msg_entry.grid(row=1, column=0)

        self.send_button = tk.Button(self.root, text="送信", command=self.send_message)
        self.send_button.grid(row=1, column=1)

    def send_message(self):
        message = self.msg_entry.get()
        if message:
            self.update_chat_log(f"あなた: {message}\n")
            self.msg_entry.delete(0, tk.END)
            self.respond_to_message(message)

    def update_chat_log(self, message):
        self.chat_log.config(state='normal')
        self.chat_log.insert(tk.END, message)
        self.chat_log.yview(tk.END)
        self.chat_log.config(state='disabled')

    def respond_to_message(self, message):
        # ユーザーの入力に応じた応答を返します。
        if "こんにちは" in message:
            response = "チャットボット: こんにちは！どうしたの？\n"
        elif "おはよう" in message:
            response = "チャットボット: おはようございます！今日も一日がんばりましょう。\n"
        elif "おやすみ" in message:
            response = "チャットボット: おやすみなさい。良い夢を。\n"
        else:
            response = "チャットボット: ごめんなさい、よくわかりません。\n"
        self.update_chat_log(response)

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatBotApp(root)
    root.mainloop()