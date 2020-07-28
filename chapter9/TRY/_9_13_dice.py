from random import randint

class Dice:
    """Create a Dice"""

    def __init__(self):
        """Create attributes"""
        self.sides = 20

    def roll_dice(self):
        """Roll the dice"""
        sides = self.sides
        print(randint(1, sides))

dobbelsteen = Dice()
for _ in range(10):
    dobbelsteen.roll_dice()
