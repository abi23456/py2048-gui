class Board:
    def __init__(self, size=4):
        self.size = size
        self.board = self.initialize_board()
        self.add_random_tile()
        self.add_random_tile()

    def initialize_board(self):
        return [[0] * self.size for _ in range(self.size)]

    def add_random_tile(self):
        import random
        empty_tiles = [(i, j) for i in range(self.size) for j in range(self.size) if self.board[i][j] == 0]
        if empty_tiles:
            i, j = random.choice(empty_tiles)
            self.board[i][j] = random.choice([2, 4])

    def move(self, direction):
        # Implement movement logic here
        pass

    def merge_tiles(self):
        # Implement tile merging logic here
        pass

    def is_full(self):
        return all(self.board[i][j] != 0 for i in range(self.size) for j in range(self.size))

    def reset(self):
        self.board = self.initialize_board()
        self.add_random_tile()
        self.add_random_tile()