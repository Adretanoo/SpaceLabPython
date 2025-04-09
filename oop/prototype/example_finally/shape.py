import copy


class ShapePrototype:
    def __init__(self, color, x, y, shape):
        self.color = color
        self.x = x
        self.y = y
        self.shape = shape


    def clone(self):
        return copy.copy(self)

    def deep_clone(self):
        return copy.deepcopy(self)
