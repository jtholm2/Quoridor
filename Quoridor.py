# Author: James Holmes
# Date: 8/7/2021
# Description: This project contains functionality that allows for the playing of a game called Quoridor.

class QuoridorGame:
    """
        This class represents Quoridor and includes functionality that allows for the game play. It is composed of 2
        Player objects and a Board object to help organize.
    """

    def __init__(self):
        """Initializes the start of the game"""
        self._p1 = Player('P1')
        self._p2 = Player('P2')
        self._board = Board(self._p1.get_name(), self._p2.get_name())
        self._turn = 1
        self._state = "UNFINISHED"

    def print_board(self):
        """returns the current state of the board"""
        for row in self._board.get_board():
            print(row)

    def get_player(self, player):
        """
        Retrieves the player object associated with the provided input.
        :param player: Integer representing the player to retrieve.
        :return: Returns the player object based on the provided input.
        """
        if player == 1:
            return self._p1

        elif player == 2:
            return self._p2

        return None

    def move_pawn(self, player, location):
        """
        This method allows a player to move or not move their pawn.
        @param player: This is a numerical value 1 or 2 representing the player making the move.
        @param location: Needs to be a tuple value representing the square the player wants to move the piece.
        @return: False if the move is forbidden, blocked by a fence, or the game has already been won. True if the move
        was successful, or if the move makes the player win.
        """

        if player != self._turn or self._state == "FINISHED":
            return False

        pawn = self.get_player(player)
        pawn_name = pawn.get_name()

        result = self._board.make_move(pawn, location)

        if result:
            winning_state = self._board.check_win(pawn)
            # if the move was successful, make it the other player's turn
            self._turn = 2 if player == 1 else 1
            return True

        return False

    def place_fence(self, player, fence, location):
        """
        @param player: This is a numerical value 1 or 2 representing the player making the move.
        @param fence: This is a string value 'v' or 'h' to represent the type of fence to be placed.
        @param location: This is a tuple value representing the square the player wants to place the fence.
        @return:
        """

        if player != self._turn or self._state == "FINISHED":
            return False

        pawn = self.get_player(player)
        result = self._board.place_fence(pawn, fence, location)

        if result:
            # if the move was successful, make it the other player's turn
            self._turn = 2 if player == 1 else 1
            return True

        return False

    def is_winner(self, player):
        """
        Checks to see if the provided player has won!
        :param player: Integer representing the player.
        :return: Returns True if the player has won, False otherwise.
        """
        pawn = self.get_player(player)

        return pawn.get_winner_state()


class Player:
    """
        This class represents a player of the game Quoridor. The QuoridorGame class will be composed of 2 Player objects
        to represent the two players playing the game.
    """

    def __init__(self, name):
        """Instantiates a player object with the provided name input."""
        self._name = name
        self._pieces_left = 10
        self._winner = False

    def get_pieces_left(self):
        """Returns the current number of pieces left to play."""
        return self._pieces_left

    def sub_pieces(self):
        """Subtracts the number of total pieces by 1 after the player makes a move."""
        self._pieces_left -= 1

    def get_name(self):
        """Returns the player's name."""
        return self._name

    def get_winner_state(self):
        """Returns if this player is a winner or not."""
        return self._winner

    def set_winner_state(self, won):
        """
        Sets the state if the Player won the game.
        :param won: Bool representing the winning state. **NOTE** This is only used to modify it from False to True.
        :return: None
        """
        self._winner = won


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
        elif current_loc[1] + 1 == new_loc[1] and (new_loc[0], new_loc[1] + 1) not in self._horiz_fences:
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

        if self._board[current_loc[0]][current_loc[1]+1] == " " and self._board[current_loc[0]][current_loc[1]-1] == " ":
            # invalid diagonal move
            return False

        if current_loc[0] + 1 == new_loc[0]:
            if (current_loc[1] + 1 == new_loc[1] or current_loc[1] - 1 == new_loc[1]) and new_loc not in self._vert_fences:
                return True

        elif current_loc[0] - 1 == new_loc[0]:
            if current_loc[1] + 1 == new_loc[1] or current_loc[1] - 1 == new_loc[1] == new_loc[1]:
                if (current_loc[0], current_loc[1] + 1) not in self._vert_fences:
                    return True

        return False

    def place_fence(self, player, fence, location):
        """
        This method validates the move and then places the fence accordingly.
        :param player: The Player object making the move.
        :param fence: A string object representing the type of fence being placed.
        :param location: A tuple representing where the player wants to place the fence.
        :return: Makes the move and then returns True if it is valid and returns False otherwise.
        """

        if player.get_pieces_left() == 0 or location in self._vert_fences or location in self._horiz_fences:
            return False

        if fence == 'v':
            if location[0] < 1 or location[0] > 8 or location[1] < 0 or location[1] > 8:
                return False

            self._vert_fences.append(location)

        elif fence == 'h':
            if location[0] < 0 or location[0] > 8 or location[1] < 1 or location[1] > 8:
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



q = QuoridorGame()
q.move_pawn(1, (4, 1))
q.move_pawn(2, (4, 7))

q.move_pawn(1, (4, 2))
q.move_pawn(2, (4, 6))

q.move_pawn(1, (4, 3))
q.move_pawn(2, (4, 5))

q.move_pawn(1, (4, 4))
q.place_fence(2, 'h', (7, 1))
q.print_board()
q.place_fence(1, 'h', (4, 4))
q.move_pawn(2, (3, 4))
q.print_board()