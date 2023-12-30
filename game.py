import tkinter as tk
from tkinter import messagebox
from board import TicTacToeBoard
from player import Player
from ai import ComputerPlayer

# Common styling options for buttons
BUTTON_STYLE = {
    "bg": "green3",
    "fg": "white",
    "font": ("Helvetica", 18, "bold"),
    "width": 10,
}

LABEL_STYLE = {"font": ("Helvetica", 26), "fg": "#D21404"}


class TicTacToeGame:
    """
    Represents the Tic Tac Toe game

    Attributes
    ----------
    master(tk.Tk): The main Tkinter window.
    player_one_squares (list): List of cell indices markedby player one.
    player_two_squares (list): List of cell indices markedby player two.

    Methods
    ----------
    __init__(): Initializes a new instance of the TicTacToeGame class.

    main_menu(): Creates the main menu when the program gets opened or a game ends.

    new_game(): Opens a window when the new game button gets clicked. Giving the
                player an option to have a 2 player game, play against an easy
                or hard AI.

    release_grab(): Enables interaction with the main menu after the new game
    window is closed.

    two_player_game(): Starts a 2 player game after this option gets chosen.

    easy_ai_game(): Starts a game against an easy AI opponent.

    hard_ai_game(): Starts a game against an hard AI opponent.

    handle_turn(): Plays out a player turn once they press one of the buttons on the board.

    check_winner(): After a turn check if 1 of the players won the game.
    """

    def __init__(self, master):
        """
        Initializes a new instance of the TicTacToeGame class.

        Parameters
        ----------
        master(tk.Tk): The main Tkinter window.
        """
        self.master = master
        self.master.title("Tic Tac Toe")
        self.master.geometry("800x800")
        self.current_player = "player_one"
        self.player_one_squares = []
        self.player_two_squares = []
        self.main_menu()
        self.game_mode = ""

    def main_menu(self):
        """
        Creates the main menu when the program gets opened or a game ends.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        self.master.welcome_label = tk.Label(
            text="Welcome to Tic Tac Toe!", **LABEL_STYLE
        )
        self.master.welcome_label.grid(row=0, column=0, pady=(300, 10), padx=200)

        # Add new game button
        self.master.new_game_button = tk.Button(
            text="New Game", command=self.new_game, **BUTTON_STYLE
        )
        self.master.new_game_button.grid(row=1, column=0)

    def new_game(self):
        """
        Opens a window when the new game button gets clicked. Giving the
        player an option to have a 2 player game, play against an easy
        or hard AI.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """

        # Create new window
        self.new_window = tk.Toplevel(self.master)
        self.new_window.geometry("400x400")
        # Disable interaction with the main window
        self.master.attributes("-disabled", 1)
        # Make the new game window modal
        self.new_window.grab_set()

        # Add label that prompts game mode choice
        self.choose_mode_label = tk.Label(
            self.new_window, text="Choose a mode", **LABEL_STYLE
        )
        self.choose_mode_label.grid(row=0, column=0, padx=80, pady=(20, 20))

        # Add 2 player button
        self.two_players_button = tk.Button(
            self.new_window,
            text="2 Players",
            **BUTTON_STYLE,
            command=self.two_player_game,
        )
        self.two_players_button.grid(row=1, column=0, pady=(0, 20))

        # Add Easy AI button
        self.easy_ai_button = tk.Button(
            self.new_window, text="Easy AI", **BUTTON_STYLE, command=self.easy_ai_game
        )
        self.easy_ai_button.grid(row=2, column=0, pady=(0, 20))

        # Add Hard AI button
        self.hard_ai_button = tk.Button(
            self.new_window, text="Hard AI", **BUTTON_STYLE, command=self.hard_ai_game
        )
        self.hard_ai_button.grid(row=3, column=0, pady=(0, 20))

        # Release the grab when the new game window is closed
        self.new_window.protocol("WM_DELETE_WINDOW", self.release_grab)

    def release_grab(self):
        """
        Enables interaction with the main menu after the new game
        window is closed

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        self.master.attributes("-disabled", 0)
        self.new_window.destroy()

    def two_player_game(self):
        """
        Starts a 2 player game after this option gets chosen.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        self.board = TicTacToeBoard(self.master)
        self.game_mode = "two player"
        self.player_one = Player(1)
        self.player_two = Player(2)
        self.board.create_board(self.player_one, game_instance=self)
        self.release_grab()

    def easy_ai_game(self):
        """
        Starts a game against an easy AI opponent

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        self.board = TicTacToeBoard(self.master)
        self.game_mode = "easy ai"
        self.player_one = Player(1)
        self.easy_ai = ComputerPlayer("easy")
        self.board.create_board(self.player_one, game_instance=self)
        self.release_grab()

    def hard_ai_game(self):
        """
        Starts a game against an hard AI opponent

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        self.board = TicTacToeBoard(self.master)
        self.game_mode = "hard ai"
        self.player_one = Player(1)
        self.hard_ai = ComputerPlayer("hard")
        self.board.create_board(self.player_one, game_instance=self)
        self.release_grab()

    def handle_turn(self, num):
        """
        Handles a player's turn.

        Parameters
        ----------
        num (int): The index of the selected button.

        Returns
        -------
        None
        """
        if self.board.buttons[num].cget("text") != "":
            messagebox.showwarning("Cell Taken", "Please select an empty cell")
            return

        # Handle player one turn
        if self.current_player == "player_one":
            self.board.buttons[num].config(
                text="X", font=("Helvetica", 73), width=3, height=1, fg="red"
            )
            self.player_one_squares.append(num)
            if self.game_mode == "two player":
                self.current_player = "player_two"
                self.board.change_turn_label(self.player_two.player_name)
            elif self.game_mode == "easy ai":
                self.easy_ai.computer_turn = True
                self.easy_ai.handle_turn(self.board.buttons)
            elif self.game_mode == "hard ai":
                self.hard_ai.computer_turn = True
                self.hard_ai.handle_turn(self.board.buttons)
        # Handle player two turn
        elif self.current_player == "player_two":
            self.board.buttons[num].config(
                text="O", font=("Helvetica", 73), width=3, height=1, fg="blue"
            )
            self.current_player = "player_one"
            self.player_two_squares.append(num)
            self.board.change_turn_label(self.player_one.player_name)
        self.check_winner()

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
                messagebox.showinfo("Winner", f"{self.player_one.player_name} Wins")
                self.board.remove_gameboard()
            elif all(num in self.player_two_squares for num in row):
                messagebox.showinfo("Winner", f"{self.player_two.player_name} Wins")
                self.board.remove_gameboard()
