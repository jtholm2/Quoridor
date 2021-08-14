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