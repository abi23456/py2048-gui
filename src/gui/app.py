from tkinter import Tk, Frame, Label, Button, messagebox
from gui.controller import GameController

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("2048 Game")
        self.master.geometry("400x500")
        self.master.resizable(False, False)

        self.frame = Frame(self.master)
        self.frame.pack()

        self.score_label = Label(self.frame, text="Score: 0", font=("Arial", 24))
        self.score_label.pack()

        self.restart_button = Button(self.frame, text="Restart", command=self.restart_game, font=("Arial", 14))
        self.restart_button.pack()

        self.controller = GameController(self)

        self.update_score(0)

    def update_score(self, score):
        self.score_label.config(text=f"Score: {score}")

    def restart_game(self):
        self.controller.restart_game()

    def show_message(self, message):
        messagebox.showinfo("Game Over", message)

if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()