import unittest
from Quoridor import QuoridorGame, Player, Board


class MyTestCase(unittest.TestCase):
    def test_p1_invalid_turn(self):
        q = QuoridorGame()
        q.move_pawn(1, (4,1))
        result = q.move_pawn(1, (4,2))
        self.assertEqual(False, result)

    def test_p2_invalid_turn(self):
        q = QuoridorGame()
        result = q.move_pawn(2, (4,7))
        self.assertEqual(False, result)

    def test_p1_invalid_move(self):
        q = QuoridorGame()
        result = q.move_pawn(1, (4,2))

        self.assertEqual(False, result)

    def test_p2_invalid_move(self):
        q = QuoridorGame()
        q.move_pawn(1, (4,1))
        result = q.move_pawn(2, (3,2))
        self.assertEqual(False, result)

    def test_p1_win(self):
        q = QuoridorGame()
        q.move_pawn(1, (4,1))
        q.move_pawn(2, (3,8))

        q.move_pawn(1, (4, 2))
        q.move_pawn(2, (3, 7))

        q.move_pawn(1, (4, 3))
        q.move_pawn(2, (3, 6))

        q.move_pawn(1, (4, 4))
        q.move_pawn(2, (3, 5))

        q.move_pawn(1, (4, 5))
        q.move_pawn(2, (3, 4))

        q.move_pawn(1, (4, 6))
        q.move_pawn(2, (3, 3))

        q.move_pawn(1, (4, 7))
        q.move_pawn(2, (3, 2))

        q.move_pawn(1, (4, 8))

        result = q.is_winner(1)
        self.assertEqual(True, result)

    def test_p2_win(self):
        q = QuoridorGame()
        q.move_pawn(1, (3, 0))
        q.move_pawn(2, (4, 7))

        q.move_pawn(1, (3, 1))
        q.move_pawn(2, (4, 6))

        q.move_pawn(1, (3, 2))
        q.move_pawn(2, (4, 5))

        q.move_pawn(1, (3, 3))
        q.move_pawn(2, (4, 4))

        q.move_pawn(1, (3, 4))
        q.move_pawn(2, (4, 3))

        q.move_pawn(1, (3, 5))
        q.move_pawn(2, (4, 2))

        q.move_pawn(1, (3, 6))
        q.move_pawn(2, (4, 1))

        q.move_pawn(1, (3, 7))
        q.move_pawn(2, (4,0))

        result = q.is_winner(2)
        self.assertEqual(True, result)

    def test_p1_hop(self):
        q = QuoridorGame()
        q.move_pawn(1, (4,1))
        q.move_pawn(2, (4, 7))

        q.move_pawn(1, (4, 2))
        q.move_pawn(2, (4, 6))

        q.move_pawn(1, (4, 3))
        q.move_pawn(2, (4, 5))

        q.place_fence(1, 'v', ((1,1)))
        q.move_pawn(2, (4,4))

        result = q.move_pawn(1, (4,5))

        self.assertEqual(True, result)

    def test_p2_hop(self):
        q = QuoridorGame()
        q.move_pawn(1, (4,1))
        q.move_pawn(2, (4, 7))

        q.move_pawn(1, (4, 2))
        q.move_pawn(2, (4, 6))

        q.move_pawn(1, (4, 3))
        q.move_pawn(2, (4, 5))

        q.move_pawn(1, (4,4))
        result = q.move_pawn(2, (4,3))

        self.assertEqual(True, result)

    def test_p1_blocked_hop(self):
        q = QuoridorGame()
        q.move_pawn(1, (4, 1))
        q.move_pawn(2, (4, 7))

        q.move_pawn(1, (4, 2))
        q.move_pawn(2, (4, 6))

        q.move_pawn(1, (4, 3))
        q.move_pawn(2, (4, 5))

        q.place_fence(1, 'h', ((4, 5)))
        q.move_pawn(2, (4, 4))

        result = q.move_pawn(1, (4, 5))

        self.assertEqual(False, result)

    def test_p2_blocked_hop(self):
        q = QuoridorGame()
        q.move_pawn(1, (4, 1))
        q.move_pawn(2, (4, 7))

        q.move_pawn(1, (4, 2))
        q.move_pawn(2, (4, 6))

        q.move_pawn(1, (4, 3))
        q.move_pawn(2, (4, 5))

        q.move_pawn(1, (4,4))
        q.place_fence(2, 'h',(7, 1))

        q.place_fence(1, 'h', (4, 4))
        result = q.move_pawn(2, (4, 3))

        self.assertEqual(False, result)

    def test_p1_blocked_hop_diag_left_move(self):
        q = QuoridorGame()
        q.move_pawn(1, (4, 1))
        q.move_pawn(2, (4, 7))

        q.move_pawn(1, (4, 2))
        q.move_pawn(2, (4, 6))

        q.move_pawn(1, (4, 3))
        q.move_pawn(2, (4, 5))

        q.place_fence(1, 'h', ((4, 5)))
        q.move_pawn(2, (4, 4))

        result = q.move_pawn(1, (3, 4))

        self.assertEqual(False, result)

    def test_p2_blocked_hop_diag_left_move(self):
        q = QuoridorGame()
        q.move_pawn(1, (4, 1))
        q.move_pawn(2, (4, 7))

        q.move_pawn(1, (4, 2))
        q.move_pawn(2, (4, 6))

        q.move_pawn(1, (4, 3))
        q.move_pawn(2, (4, 5))

        q.move_pawn(1, (4, 4))
        q.place_fence(2, 'h', (7, 1))

        q.place_fence(1, 'h', (4, 4))
        result = q.move_pawn(2, (3, 4))

        self.assertEqual(True, result)

    def test_p1_blocked_hop_diag_right_move(self):
        q = QuoridorGame()
        q.move_pawn(1, (4, 1))
        q.move_pawn(2, (4, 7))

        q.move_pawn(1, (4, 2))
        q.move_pawn(2, (4, 6))

        q.move_pawn(1, (4, 3))
        q.move_pawn(2, (4, 5))

        q.place_fence(1, 'h', ((4, 5)))
        q.move_pawn(2, (4, 4))

        result = q.move_pawn(1, (5, 5))

        self.assertEqual(False, result)

    def test_p2_blocked_hop_diag_right_move(self):
        q = QuoridorGame()
        q.move_pawn(1, (4, 1))
        q.move_pawn(2, (4, 7))

        q.move_pawn(1, (4, 2))
        q.move_pawn(2, (4, 6))

        q.move_pawn(1, (4, 3))
        q.move_pawn(2, (4, 5))

        q.move_pawn(1, (4, 4))
        q.place_fence(2, 'h', (7, 1))

        q.place_fence(1, 'h', (4, 4))
        result = q.move_pawn(2, (5, 4))

        self.assertEqual(True, result)

    def test_p1_out_of_fence(self):
        q = QuoridorGame()
        q.place_fence(1, 'h', (0, 1))
        q.place_fence(2, 'h', (8, 2))

        q.place_fence(1, 'h', (1, 1))
        q.place_fence(2, 'h', (7, 2))

        q.place_fence(1, 'h', (2, 1))
        q.place_fence(2, 'h', (6, 2))

        q.place_fence(1, 'h', (3, 1))
        q.place_fence(2, 'h', (5, 2))

        q.place_fence(1, 'h', (4, 1))
        q.place_fence(2, 'h', (4, 2))

        q.place_fence(1, 'h', (5, 1))
        q.place_fence(2, 'h', (3, 2))

        q.place_fence(1, 'h', (6, 1))
        q.place_fence(2, 'h', (2, 2))

        q.place_fence(1, 'h', (7, 1))
        q.place_fence(2, 'h', (1, 2))

        q.place_fence(1, 'h', (8, 1))
        q.place_fence(2, 'h', (0, 2))

        q.place_fence(1, 'h', (5, 5))
        q.place_fence(2, 'h', (6, 5))

        result = q.place_fence(1, 'h', (7, 5))

        self.assertEqual(False, result)

    def test_p1_blocked_move(self):
        q = QuoridorGame()
        q.place_fence(1, 'h', (0, 1))
        q.place_fence(2, 'h', (8, 2))

        q.place_fence(1, 'h', (1, 1))
        q.place_fence(2, 'h', (7, 2))

        q.place_fence(1, 'h', (2, 1))
        q.place_fence(2, 'h', (6, 2))

        q.place_fence(1, 'h', (3, 1))
        q.place_fence(2, 'h', (5, 2))

        q.place_fence(1, 'h', (4, 1))
        q.place_fence(2, 'h', (4, 2))

        q.place_fence(1, 'h', (5, 1))
        q.place_fence(2, 'h', (3, 2))

        q.place_fence(1, 'h', (6, 1))
        q.place_fence(2, 'h', (2, 2))

        q.place_fence(1, 'h', (7, 1))
        q.place_fence(2, 'h', (1, 2))

        q.place_fence(1, 'h', (8, 1))
        q.place_fence(2, 'h', (0, 2))

        q.place_fence(1, 'h', (5, 5))
        q.place_fence(2, 'h', (6, 5))

        result = q.move_pawn(1, (4,1))
        self.assertEqual(False, result)

    def test_p2_blocked_move(self):
        q = QuoridorGame()
        q.place_fence(1, 'h', (4, 8))
        result = q.move_pawn(2, (4, 7))

        self.assertEqual(False, result)

    def test_off_board_move(self):
        q= QuoridorGame()
        first = q.move_pawn(1, (9,9))
        with self.subTest():
            self.assertEqual(False, first)

        q.move_pawn(1, (4,1))

        second = q.move_pawn(2, (-1, 2))
        with self.subTest():
            self.assertEqual(False, second)

    def test_p1_blocked_horizontal(self):
        q = QuoridorGame()
        q.move_pawn(1, (4,1))
        q.place_fence(2, 'v', (5,1))

        result = q.move_pawn(1, (5,1))

        self.assertEqual(False, result)

    def test_p1_pieces_left(self):
        q = QuoridorGame()
        q.place_fence(1, 'h', (3,5))
        pawn = q.get_player(1)

        self.assertEqual(9, pawn.get_pieces_left())

    def test_p2_pieces_left(self):
        q = QuoridorGame()
        q.place_fence(1, 'h', (3,5))
        pawn = q.get_player(2)

        self.assertEqual(10, pawn.get_pieces_left())

    def test_p2_invalid_fence_placement(self):
        q = QuoridorGame()
        q.place_fence(1, 'h', (3,1))
        result = q.place_fence(2, 'h', (3,1))

        self.assertEqual(False, result)

    def test_fence_off_board(self):
        q = QuoridorGame()
        vert = q.place_fence(1, 'v', (0, 0))
        horz = q.place_fence(1, 'h', (0,0))

        self.assertEqual(False, vert)
        self.assertEqual(False, horz)

    def test_p1_pieces_left_after_invalid_fence(self):
        q = QuoridorGame()
        player = q.get_player(1)

        q.place_fence(1, 'h', (0,0))

        self.assertEqual(10, player.get_pieces_left())

    def test_fence_exists_piece_no_change(self):
        q = QuoridorGame()
        player = q.get_player(2)

        q.place_fence(1, 'h', (4,1))
        q.place_fence(2, 'h', (4,1))

        self.assertEqual(10, player.get_pieces_left())

    def test_p1_moving_backwards(self):
        q = QuoridorGame()
        q.move_pawn(1, (4, 1))
        q.move_pawn(2, (4, 7))
        result = q.move_pawn(1, (4, 0))

        self.assertEqual(True, result)

    def test_p2_move_after_p1_win(self):
        q = QuoridorGame()
        q.move_pawn(1, (4, 1))
        q.move_pawn(2, (3, 8))

        q.move_pawn(1, (4, 2))
        q.move_pawn(2, (3, 7))

        q.move_pawn(1, (4, 3))
        q.move_pawn(2, (3, 6))

        q.move_pawn(1, (4, 4))
        q.move_pawn(2, (3, 5))

        q.move_pawn(1, (4, 5))
        q.move_pawn(2, (3, 4))

        q.move_pawn(1, (4, 6))
        q.move_pawn(2, (3, 3))

        q.move_pawn(1, (4, 7))
        q.move_pawn(2, (3, 2))

        q.move_pawn(1, (4, 8))

        result = q.move_pawn(2, (3,1))
        self.assertEqual(False, result)

    def test_p1_move_after_p2_win(self):
        q = QuoridorGame()
        q.move_pawn(1, (3, 0))
        q.move_pawn(2, (4, 7))

        q.move_pawn(1, (3, 1))
        q.move_pawn(2, (4, 6))

        q.move_pawn(1, (3, 2))
        q.move_pawn(2, (4, 5))

        q.move_pawn(1, (3, 3))
        q.move_pawn(2, (4, 4))

        q.move_pawn(1, (3, 4))
        q.move_pawn(2, (4, 3))

        q.move_pawn(1, (3, 4))
        q.move_pawn(2, (4, 2))

        q.move_pawn(1, (3, 6))
        q.move_pawn(2, (4, 1))

        q.move_pawn(1, (3, 7))
        q.move_pawn(2, (4, 0))

        result = q.move_pawn(1, (3,8))
        self.assertEqual(False, result)

    def test_1009(self):
        """Test that a horizontal and vertical fence can be placed in the same coordinate -- player1"""
        q = QuoridorGame()
        q.place_fence(1, 'h', (3, 3))
        q.place_fence(2, 'v', (5, 6))

        overriding_fence_move = q.place_fence(1, 'v', (3, 3))
        self.assertTrue(overriding_fence_move)

    def test_1010(self):
        """Test that a horizontal and vertical fence can be placed in the same coordinate -- player2"""
        q = QuoridorGame()
        q.place_fence(1, 'h', (3, 3))
        q.place_fence(2, 'v', (5, 6))

        q.place_fence(1, 'v', (5, 5))
        overriding_fence_move = q.place_fence(2, 'h', (5, 6))
        self.assertTrue(overriding_fence_move)

    def test_p1_cant_jump_over_fence(self):
        q = QuoridorGame()
        q.move_pawn(1, (4, 1))
        q.place_fence(2, 'h', (4, 2))  # blocking fence

        jumping_over_fence_move = q.move_pawn(1, (4, 2))
        self.assertFalse(jumping_over_fence_move)

    def test_1103(self):
        """test that pawns can move diagonally in the correct condition -- player1 -- left diagonal"""
        q = QuoridorGame()
        q.move_pawn(1, (4, 1))
        q.move_pawn(2, (4, 7))

        q.move_pawn(1, (4, 2))
        q.move_pawn(2, (4, 6))

        q.move_pawn(1, (4, 3))
        q.move_pawn(2, (4, 5))

        q.move_pawn(1, (4, 4))  # now they are face to face
        q.place_fence(2, 'h', (4, 6))  # this will block the jump by player1

        left_diagonal_move = q.move_pawn(1, (3, 5))
        self.assertTrue(left_diagonal_move)

    def test_1104(self):
        """Test that pawns can move diagonally in the correct condition -- player1 - right diagonal"""
        q = QuoridorGame()
        q.move_pawn(1, (4, 1))
        q.move_pawn(2, (4, 7))

        q.move_pawn(1, (4, 2))
        q.move_pawn(2, (4, 6))

        q.move_pawn(1, (4, 3))
        q.move_pawn(2, (4, 5))

        q.move_pawn(1, (4, 4))  # now they are face to face
        q.place_fence(2, 'h', (4, 6))  # this will block the jump by player1

        right_diagonal_move = q.move_pawn(1, (5, 5))
        self.assertTrue(right_diagonal_move)

    def test_1107(self):
        """Test that pawns can't move diagonally left in the wrong conditions -- when there is no wall blocking the jump -- player2"""
        q = QuoridorGame()
        q.move_pawn(1, (4, 1))
        q.move_pawn(2, (4, 7))

        q.move_pawn(1, (4, 2))
        q.move_pawn(2, (4, 6))

        q.move_pawn(1, (4, 3))
        q.move_pawn(2, (4, 5))

        q.move_pawn(1, (4, 4))  # now they are face to face
        q.place_fence(2, 'h', (7, 1))  # just so that we can finish the turn

        q.place_fence(1, 'h', (6, 6))  # this fence will *not* block the jump

        wrong_left_diagonal_move = q.move_pawn(2, (3, 4))
        self.assertFalse(wrong_left_diagonal_move)

    def test_1108(self):
        """Test that pawns can't move diagonally right in the wrong conditions -- when there is no wall blocking the jump -- player2"""
        q = QuoridorGame()
        q.move_pawn(1, (4, 1))
        q.move_pawn(2, (4, 7))

        q.move_pawn(1, (4, 2))
        q.move_pawn(2, (4, 6))

        q.move_pawn(1, (4, 3))
        q.move_pawn(2, (4, 5))

        q.move_pawn(1, (4, 4))  # now they are face to face
        q.place_fence(2, 'h', (7, 1))  # just so that we can finish the turn

        q.place_fence(1, 'h', (6, 6))  # this fence will *not* block the jump by player2

        wrong_right_diagonal_move = q.move_pawn(2, (5, 4))
        self.assertFalse(wrong_right_diagonal_move)


if __name__ == '__main__':
    unittest.main()
