import tkinter as tk
from tkinter import messagebox
from functools import partial


class TicTacToeBoard:
    """
    Represents the Tic Tac Toe Board

    Attributes
    ----------
    master (tk.Tk): The main Tkinter window.
    current_player (str): The current player ("player_one"or "player_two").
    buttons (list): List of button widgets representing thegame cells.
    player_one_squares (list): List of cell indices markedby player one.
    player_two_squares (list): List of cell indices markedby player two.

    Methods
    ----------
    __init__(): Initializes a new instance of the TicTacToeBoard class.

    create_board(): Creates the game board.

    handle_turn(): Plays out a player turn once they press one of the buttons on the board.

    change_turn_label(): Changes the label that indicates who's turn it is.

    check_winner(): After a turn check if 1 of the players won the game.

    remove_gameboard(): Clears the gameboard once a game is finished to make room for the main menu.
    """

    def __init__(self, master):
        """
        Initializes a new instance of the TicTacToeBoard class.

        Parameters
        ----------
        master(tk.Tk): The main Tkinter window.

        Returns
        -------
        None
        """
        self.master = master
        self.current_player = "player_one"
        self.buttons = []
        self.player_one_squares = []
        self.player_two_squares = []

    def create_board(self, player_one, player_two, game_instance):
        """
        Creates the Tic Tac Toe game board.

        Parameters
        ----------
        player_one (Player): The first player.
        player_two (Player): The second player
        game_instance (_type_): The main game application instance

        Returns
        -------
        None
        """
        self.game_instance = game_instance

        # Create a frame for the board
        self.board_frame = tk.Frame(self.master)
        self.board_frame.grid(row=0, column=0, padx=125, pady=50)

        # Remove main menu widgets
        self.master.new_game_button.grid_remove()
        self.master.welcome_label.grid_remove()

        # Add buttons / game board
        row_number = 0
        column_number = 0
        for i in range(0, 9):
            self.new_button = tk.Button(
                self.board_frame,
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

        # Add label indicating who's turn it is
        self.turn_label = tk.Label(
            self.master,
            text=f"{player_one.player_name} it is your turn.",
            font=("Helvetica", 26),
            fg="#D21404",
        )
        self.turn_label.grid(row=3, column=0)

    def handle_turn(self, num, player_one, player_two):
        """
        Handles a player's turn.

        Parameters
        ----------
        num (int): The index of the selected button.
        player_one (Player): The first player.
        player_two (Player): The second player.

        Returns
        -------
        None
        """
        # Handle player one turn
        if self.buttons[num].cget("text") == "":
            if self.current_player == "player_one":
                self.buttons[num].config(
                    text="X", font=("Helvetica", 73), width=3, height=1, fg="red"
                )
                self.current_player = "player_two"
                self.player_one_squares.append(num)
                self.change_turn_label(player_two.player_name)
            # Handle player two turn
            elif self.current_player == "player_two":
                self.buttons[num].config(
                    text="O", font=("Helvetica", 73), width=3, height=1, fg="blue"
                )
                self.current_player = "player_one"
                self.player_two_squares.append(num)
                self.change_turn_label(player_one.player_name)
            self.check_winner()
        else:
            messagebox.showwarning("Cell Taken", "Please select an empty cell")

    def change_turn_label(self, player_name):
        """
        Changes the the turn label

        Parameters
        ----------
        player_name (str): The name of the player who's turn it is.

        Returns
        -------
        None
        """
        self.turn_label.config(text=f"{player_name} it is your turn.")

    def check_winner(self):
        """
        Checks if the player who just had a turn won the game.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        winning_conditions = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6),
        ]

        for row in winning_conditions:
            if all(num in self.player_one_squares for num in row):
                messagebox.showinfo("Winner", "Player One Wins")
                self.remove_gameboard()
            elif all(num in self.player_two_squares for num in row):
                messagebox.showinfo("Winner", "Player Two Wins")
                self.remove_gameboard()

    def remove_gameboard(self):
        """
        Clears the gameboard once a game is finished to make room for the main menu.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        for button in self.buttons:
            button.grid_remove()
        self.turn_label.grid_remove()
        self.board_frame.grid_remove()
        self.game_instance.main_menu()
