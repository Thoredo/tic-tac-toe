from tkinter.simpledialog import askstring


class Player:
    """
    A class to represent a player.

    Attributes
    ----------
    player_number(int): Number that shows if player 1 or 2 is playing.
    player_name(str): The name of the player obtained throught user input.
    """

    def __init__(self, number):
        """
        Constructs the necessary attributes for the player object

        Parameters
        ----------
        number(int): The number the player gets assigned when creating an instance
        """
        self.player_number = number
        self.player_name = askstring(
            "Name", f"What is the name of player {self.player_number}"
        )
        if self.player_name == "":
            self.player_name = f"Player {self.player_number}"
