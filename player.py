from tkinter.simpledialog import askstring


class Player:
    def __init__(self, number):
        self.player_number = number
        self.player_name = askstring(
            "Name", f"What is the name of player {self.player_number}"
        )
