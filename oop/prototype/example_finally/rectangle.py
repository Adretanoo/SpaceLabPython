from shape import ShapePrototype


class Rectangle(ShapePrototype):
    def __init__(self, color, x, y):
        super().__init__(color, x, y, "rectangle")
