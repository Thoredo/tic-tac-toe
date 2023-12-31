import random

BUTTON_OPTIONS = {
    "text": "O",
    "font": ("Helvetica", 73),
    "width": 3,
    "height": 1,
    "fg": "blue",
}


class ComputerPlayer:
    def __init__(self, difficulty):
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

    def handle_turn(self, buttons, player_squares=None):
        if self.difficulty == "easy":
            self.fill_random_square(buttons)
        if self.difficulty == "hard":
            if self.turn_number == 1:
                if player_squares[0] in self.corner_numbers:
                    buttons[4].config(**BUTTON_OPTIONS)
                    self.turn_number += 1
                    return 4
                else:
                    random_corner = random.choice(self.corner_numbers)
                    buttons[random_corner].config(**BUTTON_OPTIONS)
                    self.turn_number += 1
                    return random_corner
            else:
                computer_victory_row = self.check_win_chances(buttons, "O")
                player_victory_row = self.check_win_chances(buttons, "X")
                if computer_victory_row != None:
                    button_index = self.play_optimal_move(buttons, computer_victory_row)
                    return button_index
                elif player_victory_row != None:
                    button_index = self.play_optimal_move(buttons, player_victory_row)
                    return button_index
                else:
                    self.fill_random_square(buttons)

    def check_win_chances(self, buttons, symbol):
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
        while self.computer_turn:
            random_number = random.randint(0, 8)
            if buttons[random_number].cget("text") == "":
                buttons[random_number].config(**BUTTON_OPTIONS)
                self.computer_turn = False
                return random_number
            if all(button.cget("text") != "" for button in buttons):
                self.computer_turn = False

    def play_optimal_move(self, buttons, victory_row):
        for button_index in victory_row:
            if buttons[button_index].cget("text") == "":
                buttons[button_index].config(**BUTTON_OPTIONS)
                return button_index
