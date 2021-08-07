# Author: James Holmes
# Date: 8/6/2021
# Description: This project contains functionality that allows for the playing of a game called Quoridor.

"""
HALFWAY PROGRESS REPORT QUESTIONS

1.	Determining how to store the board.
    The board is stored as a Board object in a private variable in the QuoridorGame class. (Line 32)
2.	Initializing the board.
    I hard coded the intialization of the board when the QuoridorGame class is instantiated. (Line 119-129)
3.	Determining how to track which player’s turn it is to play right now.
    I decided to track this via the private variable 'turn' in the QuoridorGame class.
4.	Determining how to validate a moving of the pawn.
    I have a series of methods in the Board class that validate each movement (vertical, horizontal, or diagonal)
    dependent on the provided tuple. (Lines 145-253).
5.	Determining how to validate placing of the fences.
    I don't have a method for this complete yet (it's in my TO DO!), but I plan on first verifying that the player
    making the move has pieces left to play, then validating that a fence doesn't already exist in that position before
    finally placing the fence.
6.	Determining how to keep track of fences on the board and off the board.
    I'm keeping track of fences off the board by storing that as a private variable in each of the Player objects.
    I'll be keeping track of the fences on the board via 2 lists in my Board object - one for vertical fences and one
    for horizontal fences.
7.	Determining how to keep track of the pawn’s position on the board.
    I'll be keeping track of the pawn's position on the board via the list of lists I initialized when I instantiated
    the QuoridorGame class and the Board class.
"""

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

        result = self._board.make_move(player, location)
        if result:
            self._turn = 2 if player == 1 else 1
            return True

        return False

    def place_fence(self, player, fence, location):
        """
        @param player:
        @param fence:
        @param location:
        @return:
        """
        # TODO add functionality to support the adding of fences
        return 0

    def is_winner(self, player):
        """
        Checks to see if the provided player has won!
        :param player: Integer representing the player.
        :return: Returns True if the player has won, False otherwise.
        """
        if player == 1:
            return self._p1.get_winner_state()

        return self._p2.get_winner_state()


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

    def get_pieces(self):
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
        pawn = 'P1' if player == 1 else "P2"
        current_loc = self.get_current_location(pawn)
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
            self._board[new_loc[1]][new_loc[0]] = pawn
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

        if self._board[current_loc[0]][current_loc[1] + 1] == " ":
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

    def check_win(self):
        """
        Used to see if there is a winner!
        :return: True if there is a winner, False otherwise.
        """
        # TODO Add functionality to check if a player has won and change their state.


q = QuoridorGame()
print(q.move_pawn(2, (4,7))) # moves the Player2 pawn -- invalid move because only Player1 can start, returns False
print(q.move_pawn(1, (4,1))) # moves the Player1 pawn -- valid move, returns True
