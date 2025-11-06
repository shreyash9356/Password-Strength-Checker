import tkinter as tk
from tkinter import messagebox
import string

def check_password_strength(password):
    length = len(password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)
    score = sum([has_upper, has_lower, has_digit, has_special])

    if length < 8:
        return "Weak (Too short)"
    elif score == 1 or score == 2:
        return "Weak"
    elif score == 3:
        return "Medium"
    else:
        return "Strong"

def check_strength():
    password = entry.get()
    if not password:
        messagebox.showwarning("Warning", "Please enter a password!")
        return
    strength = check_password_strength(password)
    result_label.config(text=f"Password Strength: {strength}")

def clear_text():
    entry.delete(0, tk.END)
    result_label.config(text="")

# GUI Window
root = tk.Tk()
root.title("🔒 Password Strength Checker")
root.geometry("400x250")
root.config(bg="#1E1E1E")

# Heading
title_label = tk.Label(root, text="Password Strength Checker", font=("Arial", 16, "bold"), fg="#00FFAA", bg="#1E1E1E")
title_label.pack(pady=10)

# Input Box
entry = tk.Entry(root, show="*", width=30, font=("Arial", 12), relief="flat", justify="center")
entry.pack(pady=10)

# Buttons
check_button = tk.Button(root, text="Check Strength", command=check_strength, bg="#00FFAA", fg="#000", font=("Arial", 10, "bold"), relief="flat", width=15)
check_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear", command=clear_text, bg="#FF5555", fg="#fff", font=("Arial", 10, "bold"), relief="flat", width=15)
clear_button.pack(pady=5)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 12, "bold"), fg="#FFF", bg="#1E1E1E")
result_label.pack(pady=15)

# Run GUI
root.mainloop()
