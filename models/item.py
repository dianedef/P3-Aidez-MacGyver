class Item:
    def __init__(self, name, position):
        """ This function initialize an Item with a name, a position and a status (catched or not)"""
        self.name = name
        self.position = position
        self.status = "not_catched"

    def __eq__(self, other):
        """ This function allows to compare two positions on the basis of their x and y """
        if self.position.x == other.x and self.position.y == other.y:
            return True