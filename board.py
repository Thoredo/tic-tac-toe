import tkinter as tk
from functools import partial


class TicTacToeBoard:
    """
    Represents the Tic Tac Toe Board

    Attributes
    ----------
    master (tk.Tk): The main Tkinter window.
    current_player (str): The current player ("player_one"or "player_two").
    buttons (list): List of button widgets representing thegame cells.

    Methods
    ----------
    __init__(): Initializes a new instance of the TicTacToeBoard class.

    create_board(): Creates the game board.

    change_turn_label(): Changes the label that indicates who's turn it is.

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
        self.buttons = []

    def create_board(self, player_one, game_instance):
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
                command=partial(self.game_instance.handle_turn, i),
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
        self.game_instance.current_player = "player_one"
        self.game_instance.player_one_squares = []
        self.game_instance.player_two_squares = []
        self.game_instance.computer_squares = []
        self.game_instance.main_menu()
