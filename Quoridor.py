# Author: James Holmes
# Date: 8/7/2021
# Description: This project contains functionality that allows for the playing of a game called Quoridor.
from Player import Player
from Board import Board


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
            if winning_state:
                self._state = "FINISHED"

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

