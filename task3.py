import tkinter as tk
from tkinter import messagebox
import string

def check_strength(password):
    length = len(password) >= 8
    lowercase = any(c.islower() for c in password)
    uppercase = any(c.isupper() for c in password)
    digit = any(c.isdigit() for c in password)
    special = any(c in string.punctuation for c in password)

    score = sum([length, lowercase, uppercase, digit, special])
    
    if score <= 2:
        return "Weak", "red"
    elif score == 3 or score == 4:
        return "Medium", "orange"
    else:
        return "Strong", "green"

def evaluate_password():
    pwd = entry.get()
    if not pwd:
        messagebox.showwarning("Input Error", "Please enter a password!")
        return
    strength_text, color = check_strength(pwd)
    result_label.config(text=f"Strength: {strength_text}", fg=color)

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x250")
root.config(bg="#f5f5f5")

title = tk.Label(root, text="🔐 Password Strength Checker", font=("Helvetica", 16, "bold"), bg="#f5f5f5", fg="#333")
title.pack(pady=20)

entry = tk.Entry(root, font=("Helvetica", 14), width=30)
entry.pack(pady=10)

check_btn = tk.Button(root, text="Check Strength", command=evaluate_password, bg="#007bff", fg="white", font=("Helvetica", 12), padx=10, pady=5)
check_btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 14, "bold"), bg="#f5f5f5")
result_label.pack(pady=10)

root.mainloop()
