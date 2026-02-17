import unittest
from knight_m import knight_moves

class TestKnightMoves(unittest.TestCase):
    def test_center_position(self):
        moves = knight_moves((4, 4))
        expected = [
            (6, 5), (5, 6), (3, 6), (2, 5),
            (2, 3), (3, 2), (5, 2), (6, 3)
        ]
        self.assertCountEqual(moves, expected)

    def test_corner_position(self):
        moves = knight_moves((0, 0))
        expected = [(2, 1), (1, 2)]
        self.assertCountEqual(moves, expected)

    def test_edge_position(self):
        moves = knight_moves((0, 1))
        expected = [(2, 2), (2, 0), (1, 3)]
        self.assertCountEqual(moves, expected)

if __name__ == "__main__":
    unittest.main()