import tkinter as tk


class TicTacToeApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.master.geometry("800x800")

        self.master.welcome_label = tk.Label(
            text="Welcome to Tic Tac Toe!", font=("Helvetica", 26), fg="#D21404"
        )
        self.master.welcome_label.grid(row=0, column=0, pady=(300, 10), padx=200)

        self.master.new_game_button = tk.Button(
            text="New Game",
            bg="green3",
            fg="white",
            font=("Helvetica", 18, "bold"),
            command=self.new_game,
        )
        self.master.new_game_button.grid(row=1, column=0)

    def new_game(self):
        self.new_game_window = tk.Toplevel()
