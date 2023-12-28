import tkinter as tk


class TicTacToeApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.master.geometry("800x800")

        self.master.welcome_label = tk.Label(
            text="Welcome to Tic Tac Toe!", font=("Helvetica", 26), fg="#D21404"
        )
        self.master.welcome_label.grid(row=0, column=0, pady=(300, 10))

        self.master.new_game_button = tk.Button(text="New Game")
        self.master.new_game_button.grid(row=1, column=0, padx=375)
