import random
import tkinter as tk

def generate_password():
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%^&*()_+-="

    string = lower + upper + numbers + symbols
    length = 16

    password = "".join(random.sample(string, length))
    password_label.config(text="This is your new password: " + password)

root = tk.Tk()

password_label = tk.Label(root, text="")
password_label.pack()

regenerate_button = tk.Button(root, text="Regenerate", command=generate_password)
regenerate_button.pack()

root.mainloop()