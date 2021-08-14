class Board:
    """
        This class represents the board used to play the game Quoridor. This is where the board and used fences are
        stored and where player moves are validated.
    """

    def __init__(self, player1, player2):
        """Instantiates a board object"""
        self._board = [
            [" ", " ", " ", " ", player1, " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", player2, " ", " ", " ", " "]
        ]
        self._vert_fences = []
        self._horiz_fences = []

    def get_board(self):
        """Returns the current state of the board."""
        return self._board

    def make_move(self, player, new_loc):
        """
        Validates the move and then makes a move accordingly.
        @param player: Integer representing the player making the move.
        @param new_loc: Tuple representing the location the player wishes to move.
        @return: Returns a True/False based on whether or not it was able to successfully make a move.
        """
        # first checks to see if the new location is off the playing board
        if new_loc[0] < 0 or new_loc[1] > 8:
            return False

        pawn_name = player.get_name()
        current_loc = self.get_current_location(pawn_name)
        is_valid = False

        if current_loc == 0 or current_loc == new_loc or self._board[new_loc[1]][new_loc[0]] != " ":
            return False

        # used to validate vertical moves
        if current_loc[0] == new_loc[0]:
            is_valid = self.make_vertical_moves(current_loc, new_loc)

        # used to validate horizontal moves
        elif current_loc[1] == new_loc[1]:
            is_valid = self.make_horizontal_moves(current_loc, new_loc)

        # used to validate diagonal moves
        elif current_loc[0] + 1 == new_loc[0] or current_loc[0] - 1 == new_loc[0]:
            if current_loc[1] + 1 == new_loc[1] or current_loc[1] - 1 == new_loc[1]:
                is_valid = self.make_diagonal_moves(current_loc, new_loc)

        if is_valid:
            self._board[new_loc[1]][new_loc[0]] = pawn_name
            self._board[current_loc[1]][current_loc[0]] = " "
            return True

        return False

    def get_current_location(self, pawn):
        """
        Retrieves the current location of the inputted pawn.
        @param pawn: String representing the player (i.e. 'P1' or 'P2').
        @return: Returns a tuple of the current location.
        """
        current_loc = 0

        for row in range(len(self._board)):
            if pawn in self._board[row]:
                current_loc = (self._board[row].index(pawn), row)

        return current_loc

    def make_vertical_moves(self, current_loc, new_loc):
        """
        Checks if a vertical move is valid and then makes it.
        @param pawn: String representing the player.
        @param current_loc: Tuple representing the current location of the player.
        @param new_loc: Tuple representing where the player wants to move to.
        @return: Returns True or False depending on if the move is valid or not.
        """
        # moving backward if P1, forward if P2
        if current_loc[1] - 1 == new_loc[1] and current_loc not in self._horiz_fences:
            return True

        # moving forward if P1, backward if P2
        elif current_loc[1] + 1 == new_loc[1] and new_loc not in self._horiz_fences:
            return True

        elif current_loc[1] + 2 == new_loc[1] and self._board[current_loc[1] + 1][current_loc[0]] != " ":
            if (current_loc[1]+1, current_loc[0]) not in self._horiz_fences:
                return True

        elif current_loc[1] - 2 == new_loc[1] and self._board[current_loc[1] - 1][current_loc[0]] != " ":
            if (current_loc[1]-1, current_loc[0]) not in self._horiz_fences:
                return True

        return False

    def make_horizontal_moves(self, current_loc, new_loc):
        """
        Checks if a horizontal move is valid and then makes it.
        @param pawn: String representing the player.
        @param current_loc: Tuple representing the current location of the player.
        @param new_loc: Tuple representing where the player wants to move to.
        @return: Returns True or False depending on if the move is valid or not.
        """
        if current_loc[0] - 1 == new_loc[0] and current_loc not in self._vert_fences:
            return True

        elif current_loc[0] + 1 == new_loc[0] and (current_loc[0] + 1, current_loc[1]) not in self._vert_fences:
            return True

        return False

    def make_diagonal_moves(self, current_loc, new_loc):
        """
        Checks if a diagonal move is valid and then makes it.
        @param pawn: String representing the player.
        @param current_loc: Tuple representing the current location of the player.
        @param new_loc: Tuple representing where the player wants to move to.
        @return: Returns True or False depending on if the move is valid or not.
        """
        left_diag = 0
        right_diag = 0

        # checks validity of a left diagonal move
        if current_loc[1] + 1 == new_loc[1] or current_loc[1] - 1 == new_loc[1]:
            if new_loc not in self._vert_fences:
                left_diag = True

        # checks validity of a right diagonal move
        elif current_loc[1] + 1 == new_loc[1] or current_loc[1] - 1 == new_loc[1]:
            if (current_loc[0], current_loc[1] + 1) not in self._vert_fences:
                right_diag = True

        type_of_diag_move = left_diag if right_diag == 0 else right_diag

        # checks the up diagonal
        if new_loc[1] == current_loc[1] - 1 and self._board[current_loc[1]-1][current_loc[0]] != " ":
            if (current_loc[0], current_loc[1]-1) in self._horiz_fences:
                return type_of_diag_move

        # checks the down diagonal
        if new_loc[1] == current_loc[1] + 1 and self._board[current_loc[1]+1][current_loc[0]] != " ":
            if (current_loc[0], current_loc[1] + 2) in self._horiz_fences:
                return type_of_diag_move

        return False

    def place_fence(self, player, fence, location):
        """
        This method validates the move and then places the fence accordingly.
        :param player: The Player object making the move.
        :param fence: A string object representing the type of fence being placed.
        :param location: A tuple representing where the player wants to place the fence.
        :return: Makes the move and then returns True if it is valid and returns False otherwise.
        """

        if player.get_pieces_left() == 0:
            return False

        if fence == 'v':
            if location[0] < 1 or location[0] > 8 or location[1] < 0 or location[1] > 8 or location in self._vert_fences:
                return False

            self._vert_fences.append(location)

        elif fence == 'h':
            if location[0] < 0 or location[0] > 8 or location[1] < 1 or location[1] > 8 or location in self._horiz_fences:
                return False

            self._horiz_fences.append(location)

        player.sub_pieces()
        return True

    def check_win(self, pawn):
        """
        Used to see if there is a winner!
        :param pawn: Represents the Player object to check if they won the game.
        :return: Modifies the Player object's state if they won and then returns True, but returns False otherwise.
        """
        pawn_name = pawn.get_name()
        if pawn_name == 'P1' and pawn_name not in self._board[-1]:
            return False

        elif pawn_name == 'P2' and pawn_name not in self._board[0]:
            return False

        pawn.set_winner_state(True)
        return True