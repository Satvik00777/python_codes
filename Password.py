import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_and_display_password():
    try:
        username = username_entry.get().strip()
        password_length = int(length_entry.get())
        if password_length <= 0:
            messagebox.showerror("Invalid Input", "Password length must be a positive integer.")
            return

        password = generate_password(password_length)
        password_display_label.config(text="Generated Password for {}: {}".format(username, password))
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid positive integer.")

# Create the main application window
root = tk.Tk()
root.title("Password Generator")

# Create widgets
username_label = tk.Label(root, text="Enter your username:")
username_label.pack()

username_entry = tk.Entry(root)
username_entry.pack()

length_label = tk.Label(root, text="Enter the desired length of the password:")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_and_display_password)
generate_button.pack()

password_display_label = tk.Label(root, text="")
password_display_label.pack()

# Start the main event loop
root.mainloop()
