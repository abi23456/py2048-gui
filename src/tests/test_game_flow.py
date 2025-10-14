import unittest
from src.game import Game

class TestGameFlow(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_initial_board(self):
        self.assertEqual(len(self.game.board.tiles), 2)
        self.assertTrue(any(tile.value in [2, 4] for tile in self.game.board.tiles))

    def test_move_tiles(self):
        initial_tiles = self.game.board.tiles.copy()
        self.game.move('left')
        self.assertNotEqual(initial_tiles, self.game.board.tiles)

    def test_merge_tiles(self):
        self.game.board.tiles = [2, 2, 0, 0]
        self.game.move('left')
        self.assertEqual(self.game.board.tiles, [4, 0, 0, 0])

    def test_new_tile_after_move(self):
        initial_tiles = self.game.board.tiles.copy()
        self.game.move('left')
        self.assertEqual(len(self.game.board.tiles), len(initial_tiles) + 1)

    def test_win_condition(self):
        self.game.board.tiles = [1024, 1024, 0, 0]
        self.game.move('left')
        self.assertTrue(self.game.has_won())

    def test_loss_condition(self):
        self.game.board.tiles = [2, 2, 4, 4]
        self.game.move('left')
        self.game.move('right')
        self.assertTrue(self.game.is_game_over())

if __name__ == '__main__':
    unittest.main()