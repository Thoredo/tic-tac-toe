import tkinter as tk
from game import TicTacToeGame

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeGame(root)
    root.mainloop()
