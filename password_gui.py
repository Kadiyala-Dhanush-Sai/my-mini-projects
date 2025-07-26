import tkinter as tk
from tkinter import messagebox
import random

# Character pools
letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
symbols = list("!@#$%^&*()-_=+{}[]|\\:;\"',.<>/?~`")
numbers = list("0123456789")

# Password generator function
def generate_password():
    try:
        l = int(letter_entry.get())
        s = int(symbol_entry.get())
        n = int(number_entry.get())
        
        password = []
        for _ in range(l):
            password.append(random.choice(letters))
        for _ in range(s):
            password.append(random.choice(symbols))
        for _ in range(n):
            password.append(random.choice(numbers))
        
        random.shuffle(password)
        result = ''.join(password)
        output_label.config(text=f"Generated Password:\n{result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers!")

# GUI setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.resizable(False, False)

# Title
title_label = tk.Label(root, text="🔐 Password Generator", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

# Input frame
frame = tk.Frame(root)
frame.pack(pady=5)

tk.Label(frame, text="Letters:").grid(row=0, column=0, padx=5, pady=5)
letter_entry = tk.Entry(frame, width=5)
letter_entry.grid(row=0, column=1)

tk.Label(frame, text="Symbols:").grid(row=1, column=0, padx=5, pady=5)
symbol_entry = tk.Entry(frame, width=5)
symbol_entry.grid(row=1, column=1)

tk.Label(frame, text="Numbers:").grid(row=2, column=0, padx=5, pady=5)
number_entry = tk.Entry(frame, width=5)
number_entry.grid(row=2, column=1)

# Generate button
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

# Output label
output_label = tk.Label(root, text="", font=("Courier", 12), fg="green")
output_label.pack(pady=10)

# Run the app
root.mainloop()
