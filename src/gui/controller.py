# ...existing code...
from tkinter import Frame, Label
from game import Game

class GameController:
    def __init__(self, app, size=4):
        self.app = app
        self.game = Game(size)

        # Ensure the Game instance has an initialized board; try reset() if present
        if getattr(self.game, "board", None) is None:
            if hasattr(self.game, "reset"):
                self.game.reset()
            else:
                raise RuntimeError("Game.board is None after Game(); please open src/game.py")

        self.board_frame = Frame(self.app.master)
        self.board_frame.pack()
        self.update_board()
        self.app.master.bind("<Key>", self.key_press)

    def update_board(self):
        # Defensive: if board is still None, skip drawing and show a message
        if getattr(self.game, "board", None) is None:
            self.app.show_message("Internal error: game board not initialized. Check src/game.py")
            return

        for widget in self.board_frame.winfo_children():
            widget.destroy()
        for r, row in enumerate(self.game.board):
            for c, tile in enumerate(row):
                tile_value = tile if tile != 0 else ""
                label = Label(self.board_frame, text=tile_value, width=4, height=2,
                              font=("Arial", 24), borderwidth=2, relief="solid")
                label.grid(row=r, column=c, padx=5, pady=5)
        self.app.update_score(self.game.score)
        if self.game.is_game_over():
            self.app.show_message("No more moves available!")

    def key_press(self, event):
        if event.keysym in ["Up", "Down", "Left", "Right"]:
            self.game.move(event.keysym)
            self.update_board()

    def restart_game(self):
        self.game.reset()
        self.update_board()
# ...existing code...