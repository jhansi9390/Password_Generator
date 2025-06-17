import tkinter as tk
import random
import string
import pyperclip  # install with: pip install pyperclip

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            result_label.config(text="Length must be > 0")
            return
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        result_label.config(text=password)
    except ValueError:
        result_label.config(text="Enter a valid number")

def copy_to_clipboard():
    password = result_label.cget("text")
    if password and " " not in password:
        pyperclip.copy(password)
        result_label.config(text=f"{password}  ✔ Copied")

# GUI setup
root = tk.Tk()
root.title("Password Generator 🔐")
root.geometry("400x200")
root.resizable(False, False)

title = tk.Label(root, text="Password Generator", font=("Arial", 16, "bold"))
title.pack(pady=10)

frame = tk.Frame(root)
frame.pack()

tk.Label(frame, text="Password Length:", font=("Arial", 12)).grid(row=0, column=0, padx=5)
length_entry = tk.Entry(frame, font=("Arial", 12), width=5, justify="center")
length_entry.insert(0, "12")  # default length
length_entry.grid(row=0, column=1)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

generate_btn = tk.Button(btn_frame, text="Generate", font=("Arial", 12), command=generate_password)
generate_btn.grid(row=0, column=0, padx=10)

copy_btn = tk.Button(btn_frame, text="Copy 📋", font=("Arial", 12), command=copy_to_clipboard)
copy_btn.grid(row=0, column=1, padx=10)

result_label = tk.Label(root, text="", font=("Courier", 14), fg="blue")
result_label.pack(pady=10)

root.mainloop()
