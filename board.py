import tkinter as tk


class TicTacToeBoard:
    def __init__(self, master):
        self.master = master

    def create_board(self, player_one, player_two):
        # Create a frame for the board
        board_frame = tk.Frame(self.master)
        board_frame.grid(row=0, column=0, padx=125, pady=50)

        self.master.new_game_button.grid_remove()
        self.master.welcome_label.grid_remove()
        row_number = 0
        column_number = 0
        for i in range(0, 9):
            new_button = tk.Button(
                board_frame, text="", width=25, height=12, borderwidth=1, relief="solid"
            )
            new_button.grid(row=row_number, column=column_number)
            column_number += 1
            if column_number == 3:
                column_number = 0
                row_number += 1

        self.turn_label = tk.Label(
            self.master,
            text=f"{player_one.player_name} it is your turn.",
            font=("Helvetica", 26),
            fg="#D21404",
        )
        self.turn_label.grid(row=3, column=0)
