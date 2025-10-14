import unittest
from src.moves import move_left, move_right, move_up, move_down
from src.board import Board

class TestMoves(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.board.tiles = [
            [2, 2, 4, 4],
            [2, 2, 4, 4],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]

    def test_move_left(self):
        self.board.move_left()
        expected_tiles = [
            [4, 8, 0, 0],
            [4, 8, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.assertEqual(self.board.tiles, expected_tiles)

    def test_move_right(self):
        self.board.move_right()
        expected_tiles = [
            [0, 0, 4, 8],
            [0, 0, 4, 8],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.assertEqual(self.board.tiles, expected_tiles)

    def test_move_up(self):
        self.board.move_up()
        expected_tiles = [
            [4, 4, 8, 8],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.assertEqual(self.board.tiles, expected_tiles)

    def test_move_down(self):
        self.board.move_down()
        expected_tiles = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [4, 4, 8, 8],
            [0, 0, 0, 0]
        ]
        self.assertEqual(self.board.tiles, expected_tiles)

if __name__ == '__main__':
    unittest.main()