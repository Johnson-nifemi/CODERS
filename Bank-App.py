import tkinter as tk
from tkinter import messagebox


class BankApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bank App")

        self.label = tk.Label(root, text="Please choose your account type:")
        self.label.pack()

        self.savings_button = tk.Button(root, text="Savings Account", command=self.open_savings_account)
        self.savings_button.pack()

        self.current_button = tk.Button(root, text="Current Account", command=self.open_current_account)
        self.current_button.pack()

    def open_savings_account(self):
        messagebox.showinfo("Savings Account", "Please wait...")

    def open_current_account(self):
        messagebox.showinfo("Current Account", "Please wait...")


if __name__ == "__main__":
    root = tk.Tk()
    bank_app = BankApp(root)
    root.mainloop()
