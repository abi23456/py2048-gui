# ...existing code...
from tkinter import Tk
from gui.app import App

class GameApp:
    """Adapter that creates the Tk root and the App view so main.py can call GameApp().run()."""
    def __init__(self):
        self.root = Tk()
        self.app = App(self.root)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    GameApp().run()
# ...existing code...