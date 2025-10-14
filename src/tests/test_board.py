import unittest
from src.board import Board

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_initial_board(self):
        self.assertEqual(len(self.board.tiles), 2)
        self.assertTrue(all(tile in [2, 4] for tile in self.board.tiles.values()))

    def test_move_left(self):
        self.board.tiles = {
            (0, 0): 2,
            (0, 1): 2,
            (0, 2): 4,
            (0, 3): 0
        }
        self.board.move_left()
        self.assertEqual(self.board.tiles[(0, 0)], 4)
        self.assertEqual(self.board.tiles[(0, 1)], 4)
        self.assertEqual(self.board.tiles[(0, 2)], 0)

    def test_move_right(self):
        self.board.tiles = {
            (0, 0): 0,
            (0, 1): 2,
            (0, 2): 2,
            (0, 3): 4
        }
        self.board.move_right()
        self.assertEqual(self.board.tiles[(0, 2)], 4)
        self.assertEqual(self.board.tiles[(0, 3)], 4)
        self.assertEqual(self.board.tiles[(0, 0)], 0)

    def test_move_up(self):
        self.board.tiles = {
            (0, 0): 2,
            (1, 0): 2,
            (2, 0): 4,
            (3, 0): 0
        }
        self.board.move_up()
        self.assertEqual(self.board.tiles[(0, 0)], 4)
        self.assertEqual(self.board.tiles[(1, 0)], 4)
        self.assertEqual(self.board.tiles[(2, 0)], 0)

    def test_move_down(self):
        self.board.tiles = {
            (0, 0): 0,
            (1, 0): 2,
            (2, 0): 2,
            (3, 0): 4
        }
        self.board.move_down()
        self.assertEqual(self.board.tiles[(2, 0)], 4)
        self.assertEqual(self.board.tiles[(3, 0)], 4)
        self.assertEqual(self.board.tiles[(0, 0)], 0)

if __name__ == '__main__':
    unittest.main()