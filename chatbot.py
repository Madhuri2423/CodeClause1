import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
import random

# Sample predefined responses
responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm good, thanks!", "Doing well, how about you?"],
    "bye": ["Goodbye!", "See you later!", "Bye!"],
    "default": ["I'm not sure how to respond to that."]
}

def get_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return random.choice(responses["default"])

class ChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Chatbot")
        
        # Load background image
        self.background_image = Image.open("background.png")
        self.background_image = self.background_image.resize((400, 500), Image.LANCZOS)
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        self.background_label = tk.Label(root, image=self.background_photo)
        self.background_label.place(relwidth=1, relheight=1)

        # Custom fonts
        self.font = font.Font(family="Helvetica", size=12)
        self.entry_font = font.Font(family="Helvetica", size=12)

        # Chat log (scrollable)
        self.chat_frame = tk.Frame(root)
        self.chat_frame.place(x=6, y=6, height=386, width=370)
        self.chat_log = tk.Text(self.chat_frame, bd=0, bg="lightblue", fg="black", font=self.font, wrap=tk.WORD)
        self.chat_log.config(state=tk.DISABLED)
        self.scrollbar = tk.Scrollbar(self.chat_frame, command=self.chat_log.yview)
        self.chat_log['yscrollcommand'] = self.scrollbar.set
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.chat_log.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Entry box with placeholder
        self.entry_frame = tk.Frame(root, bg="lightblue", bd=1)
        self.entry_frame.place(x=6, y=401, height=50, width=300)
        self.entry_box = tk.Text(self.entry_frame, bd=0, bg="white", fg="grey", font=self.entry_font, wrap=tk.WORD)
        self.entry_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.entry_box.insert(0.0, "Type your message here...")
        self.entry_box.bind("<FocusIn>", self.clear_placeholder)
        self.entry_box.bind("<FocusOut>", self.add_placeholder)
        
        # Load send icon
        self.send_icon = Image.open("send_icon.png")
        self.send_icon = self.send_icon.resize((50, 50), Image.LANCZOS)
        self.send_photo = ImageTk.PhotoImage(self.send_icon)
        
        self.send_button = tk.Button(root, image=self.send_photo, width=50, height=50,
                                     bd=0, bg="#32de97", activebackground="#3c9d9b",
                                     command=self.send_message)
        self.send_button.place(x=315, y=401, height=50, width=50)

    def clear_placeholder(self, event):
        if self.entry_box.get("1.0", tk.END).strip() == "Type your message here...":
            self.entry_box.delete("1.0", tk.END)
            self.entry_box.config(fg="black")

    def add_placeholder(self, event):
        if not self.entry_box.get("1.0", tk.END).strip():
            self.entry_box.insert(0.0, "Type your message here...")
            self.entry_box.config(fg="grey")

    def send_message(self):
        user_input = self.entry_box.get("1.0", 'end-1c').strip()
        self.entry_box.delete("0.0", tk.END)
        
        if user_input != "":
            self.chat_log.config(state=tk.NORMAL)
            self.chat_log.insert(tk.END, "You: " + user_input + '\n\n', "user")
            self.chat_log.config(foreground="#442265", font=("Verdana", 12))
            
            response = get_response(user_input)
            self.chat_log.insert(tk.END, "Bot: " + response + '\n\n', "bot")
            
            self.chat_log.config(state=tk.DISABLED)
            self.chat_log.yview(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x500")
    app = ChatbotGUI(root)
    root.mainloop()
