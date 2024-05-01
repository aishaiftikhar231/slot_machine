import tkinter as tk
from tkinter import messagebox
import random

class SlotMachineApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Slot Machine Game")
        self.geometry("400x300")
        
        # Initialize variables
        self.balance = tk.IntVar()
        self.balance.set(100)  # Initial balance that can be changed by depositing more
        self.bet = tk.IntVar()
        self.lines = tk.IntVar()
        self.result_symbols = []

        # Create GUI elements
        self.create_widgets()

    def create_widgets(self):
        # Labels
        self.balance_label = tk.Label(self, textvariable=self.balance, fg="green", font=("Times New Roman", 20, "bold"))
        self.balance_label.pack()

        self.bet_label = tk.Label(self, text="Bet:")
        self.bet_label.pack()
        self.bet_entry = tk.Entry(self, textvariable=self.bet)
        self.bet_entry.pack()

        self.lines_label = tk.Label(self, text="Lines:")
        self.lines_label.pack()
        self.lines_entry = tk.Entry(self, textvariable=self.lines)
        self.lines_entry.pack()

        self.result_label = tk.Label(self, text="")
        self.result_label.pack()

        # Buttons
        self.deposit_button = tk.Button(self, text="Deposit", command=self.deposit)
        self.deposit_button.pack()

        self.spin_button = tk.Button(self, text="Spin", command=self.spin)
        self.spin_button.pack()

    def update_balance_label(self):
        balance = self.balance.get()
        if balance < 0:
            self.balance_label.config(text=f"Balance: ${balance}", fg="red")
        else:
            self.balance_label.config(text=f"Balance: ${balance}", fg="green")

    def deposit(self):
        deposit_amount = self.bet.get()
        self.balance.set(self.balance.get() + deposit_amount)
        self.update_balance_label()
        messagebox.showinfo("Deposit", f"Deposited ${deposit_amount} successfully!")

    def spin(self):
        bet_amount = self.bet.get()
        lines_bet = self.lines.get()

        if bet_amount <= 0 or lines_bet <= 0:
            messagebox.showerror("Error", "Bet and lines must be greater than zero.")
            return

        total_bet = bet_amount * lines_bet

        if total_bet > self.balance.get():
            messagebox.showerror("Error", "Insufficient balance to place bet.")
            return

        self.balance.set(self.balance.get() - total_bet)
        self.update_balance_label()

        self.result_symbols = []
        for _ in range(lines_bet):
            symbols = [random.choice(list(symbol_count.keys())) for _ in range(3)]
            self.result_symbols.append(symbols)

        self.show_results()

    def show_results(self):
        result_text = ""
        winnings = 0

        for i, symbols in enumerate(self.result_symbols):
            line_result = " ".join(symbols)
            result_text += f"Line {i+1}: {line_result}\n"

            if symbols[0] == symbols[1] == symbols[2]:
                winnings += symbol_count[symbols[0]] * self.bet.get()

        result_text += f"\nWinnings: ${winnings}"
        self.result_label.config(text=result_text)

# Symbol count dictionary
symbol_count = {
    "a": 2,
    "b": 9,
    "c": 7,
    "d": 5,
    "f": 4,
}

if __name__ == "__main__":
    app = SlotMachineApp()
    app.mainloop()
