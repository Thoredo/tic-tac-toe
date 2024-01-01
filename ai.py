import random

BUTTON_OPTIONS = {
    "text": "O",
    "font": ("Helvetica", 73),
    "width": 3,
    "height": 1,
    "fg": "blue",
}


class ComputerPlayer:
    """
    Represents the computer player

    Attributes
    ----------
    difficulty (str): The difficulty level of the computer player.
    computer_turn (bool): Flag to indicate whether it's the computer's turn.
    turn_number (int): The current turn number.
    corner_numbers (list): List of indices representing corners on the game board.
    side_numbers (list): List of indices representing sides on the game board.
    winning_conditions (list): List of tuples representing winning conditions on the game board.
    is_starting_player(bool): Boolean that checks if the AI is the starting player

    Methods
    ----------
    handle_turn(): Handles the computer player's turn.

    check_win_chances(): Checks the winning chances for a given symbol.

    fill_random_square(): Fills a random empty square on the game board.

    play_optimal_move(): Plays an optimal move based on a victory row.
    """

    def __init__(self, difficulty):
        """
        Initializes a new instance of the ComputerPlayer class.

        Parameters
        ----------
        difficulty (str): The difficulty level of the computer player.
        """
        self.difficulty = difficulty
        self.computer_turn = True
        self.turn_number = 1
        self.corner_numbers = [0, 2, 6, 8]
        self.side_numbers = [1, 3, 5, 7]
        self.winning_conditions = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6),
        ]
        self.is_starting_player = False

    def handle_turn(
        self,
        buttons,
        someone_won,
        player_squares=None,
    ):
        """
        Handles the computer player's turn.

        Parameters
        ----------
        buttons: The buttons representing the game board.
        someone_won (bool): Flag indicating whether someone has won.
        player_squares (list): List of indices marked by the human player.

        Returns
        -------
        button_index (int): The index of the selected button.
        """
        # Prevent the AI taking a turn if the player just won.
        if someone_won:
            return None
        # Play the easy AI's turn
        if self.difficulty == "easy":
            button_index = self.fill_random_square(buttons)
        # Play the hard AI's turn
        if self.difficulty == "hard":
            if self.is_starting_player:
                button_index = self.fill_random_square(buttons)
                self.is_starting_player = False
                return button_index
            # The playing strategy for the hard AI in their first turn
            if self.turn_number == 1:
                if player_squares[0] in self.corner_numbers:
                    buttons[4].config(**BUTTON_OPTIONS)
                    self.turn_number += 1
                    button_index = 4
                else:
                    random_corner = random.choice(self.corner_numbers)
                    buttons[random_corner].config(**BUTTON_OPTIONS)
                    self.turn_number += 1
                    button_index = random_corner
            else:
                # The playing strategy for the hard AI after their first turn.
                # It takes priority to winning the game otherwise it tries to
                # prevent the player from winning
                computer_victory_row = self.check_win_chances(buttons, "O")
                player_victory_row = self.check_win_chances(buttons, "X")
                if computer_victory_row != None:
                    button_index = self.play_optimal_move(buttons, computer_victory_row)
                elif player_victory_row != None:
                    button_index = self.play_optimal_move(buttons, player_victory_row)
                else:
                    button_index = self.fill_random_square(buttons)
        return button_index

    def check_win_chances(self, buttons, symbol):
        """
        Check if any of the winning conditions (any of the lines on the board)
        has 2 of the same symbol and an empty square.

        Parameters
        ----------
        buttons: The buttons representing the game board.
        symbol (str): The symbol to check (either "X" or "O").

        Returns
        -------
        condition (tuple): The winning condition if found, else None.
        """
        for condition in self.winning_conditions:
            condition_points = 0
            for i in range(0, 3):
                if buttons[condition[i]].cget("text") == symbol:
                    condition_points += 0.5
                elif buttons[condition[i]].cget("text") == "":
                    condition_points += 1
                else:
                    condition_points += 5
            if condition_points == 2:
                return condition

    def fill_random_square(self, buttons):
        """
        Fills a random empty square on the game board.

        Parameters
        ----------
        buttons: The buttons representing the game board.

        Returns
        -------
        button_index (int): The index of the selected button.
        """
        while self.computer_turn:
            random_number = random.randint(0, 8)
            if buttons[random_number].cget("text") == "":
                buttons[random_number].config(**BUTTON_OPTIONS)
                self.computer_turn = False
                return random_number
            if all(button.cget("text") != "" for button in buttons):
                self.computer_turn = False

    def play_optimal_move(self, buttons, victory_row):
        """
        Plays an optimal move to either win the game or prevent the player to win.

        Parameters
        ----------
        buttons: The buttons representing the game board.
        victory_row (tuple): The winning condition.

        Returns
        -------
        button_index (int): The index of the selected button.
        """
        for button_index in victory_row:
            if buttons[button_index].cget("text") == "":
                buttons[button_index].config(**BUTTON_OPTIONS)
                return button_index
