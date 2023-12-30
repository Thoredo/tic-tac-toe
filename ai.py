import random


class ComputerPlayer:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.computer_turn = True

    def handle_turn(self, buttons):
        while self.computer_turn:
            random_number = random.randint(0, 8)
            if buttons[random_number].cget("text") == "":
                buttons[random_number].config(
                    text="O", font=("Helvetica", 73), width=3, height=1, fg="blue"
                )
                self.computer_turn = False
            if all(button.cget("text") != "" for button in buttons):
                self.computer_turn = False
