# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 09:35:48 2023

@author: bryso
"""

import tkinter as tk
from tkinter import messagebox

class PinAuthenticationApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Pin Authentication App")

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.master, text="Enter Credit Card PIN:")
        self.label.pack(pady=10)

        self.pin_entry = tk.Entry(self.master, show="*")
        self.pin_entry.pack(pady=10)

        self.authenticate_button = tk.Button(self.master, text="Authenticate", command=self.authenticate_user)
        self.authenticate_button.pack(pady=10)

    def authenticate_user(self):
        entered_pin = self.pin_entry.get()

        # Replace the example PIN with the actual valid PIN
        valid_pin = "1234"

        if entered_pin == valid_pin:
            messagebox.showinfo("Authentication Successful", "PIN is valid. Access granted!")
        else:
            messagebox.showerror("Authentication Failed", "Invalid PIN. Access denied.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PinAuthenticationApp(root)
    root.mainloop()
