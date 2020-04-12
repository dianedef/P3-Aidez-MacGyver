class Position: 
    """ This class represent a position on the maze with an y and y. """

    def __init__(self, x, y):
        """ This function initialize a position with an x and y. """
        self.x = x
        self.y = y

    def update(self, direction):
        """ Cette fonction permet de faire évoluer la position d'une case vers une direction."""

        if direction == "r":
            self.x += 1
        elif direction == "l":
            self.x -= 1
        elif direction == "u":
            self.y -= 1
        elif direction == "d":
            self.y += 1

    def get_position(self):
        """ Cette fonction renvoit la position sous forme de tuple. """

        return Position(self.x, self.y)

    def __eq__(self, other):
        """ Cette fonction permet de comparer si deux positions sont identiques. """
        if self.x == other.x and self.y == other.y:
            return True

    def __repr__(self):
        """ Cette fonction renvoie la position sous forme x y"""
        
        return f"Position ({self.x}, {self.y})"

    @property
    def xy(self):
        return self.x, self.y