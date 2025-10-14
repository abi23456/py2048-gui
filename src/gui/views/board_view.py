from tkinter import Frame, Label, Tk

class BoardView:
    def __init__(self, master, board_size):
        self.master = master
        self.board_size = board_size
        self.frame = Frame(master)
        self.frame.pack()
        self.tiles = [[None for _ in range(board_size)] for _ in range(board_size)]
        self.create_board()

    def create_board(self):
        for i in range(self.board_size):
            for j in range(self.board_size):
                tile = Label(self.frame, text='', width=4, height=2, borderwidth=2, relief='ridge')
                tile.grid(row=i, column=j, padx=5, pady=5)
                self.tiles[i][j] = tile

    def update_tile(self, row, col, value):
        self.tiles[row][col].config(text=str(value) if value > 0 else '', bg=self.get_tile_color(value))

    def get_tile_color(self, value):
        colors = {
            0: '#eee4da',
            2: '#ede0c8',
            4: '#f2b179',
            8: '#f59563',
            16: '#f67c5f',
            32: '#f67c5f',
            64: '#f67c5f',
            128: '#edcf72',
            256: '#edcc61',
            512: '#edc850',
            1024: '#edc53f',
            2048: '#edc22e',
        }
        return colors.get(value, '#3c3a32')

    def clear_board(self):
        for i in range(self.board_size):
            for j in range(self.board_size):
                self.update_tile(i, j, 0)

    def display(self):
        self.master.mainloop()