import tkinter as tk
from functools import partial


class TicTacToeBoard:
    def __init__(self, master):
        self.master = master
        self.current_player = "player_one"
        self.buttons = []

    def create_board(self, player_one, player_two):
        # Create a frame for the board
        board_frame = tk.Frame(self.master)
        board_frame.grid(row=0, column=0, padx=125, pady=50)

        self.master.new_game_button.grid_remove()
        self.master.welcome_label.grid_remove()
        row_number = 0
        column_number = 0
        for i in range(0, 9):
            self.new_button = tk.Button(
                board_frame,
                text="",
                width=25,
                height=12,
                borderwidth=1,
                relief="solid",
                command=partial(self.handle_turn, i, player_one, player_two),
            )
            self.buttons.append(self.new_button)
            self.new_button.grid(row=row_number, column=column_number)
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

    def handle_turn(self, num, player_one, player_two):
        if self.current_player == "player_one":
            self.buttons[num].config(text="X")
            self.current_player = "player_two"
            self.change_turn_label(player_two.player_name)
        elif self.current_player == "player_two":
            self.buttons[num].config(text="O")
            self.current_player = "player_one"
            self.change_turn_label(player_one.player_name)

    def change_turn_label(self, player_name):
        self.turn_label.config(text=f"{player_name} it is your turn.")
