import turtle as t


class Shape:

    def __init__(self):
        self.shape = 'shape'

    def __str__(self):
        return "I am a {}.".format(self.shape)


class Polygon(Shape):

    def __init__(self):
        self.shape = 'polygon'
        self.side_lengths = None

    def compute_perimeter(self):
        return sum(self.side_lengths)

    def get_number_of_edges(self):
        return len(self.side_lengths)


class MyPolygon(Polygon):

    def __init__(self, side_lengths: list) -> None:
        super().__init__()
        if len(side_lengths) < 3:
            raise Exception("Please enter a polygon with 3 or more sides")
        self.side_lengths = side_lengths
        self.turtle = t.Turtle()

    def set_side_lengths(self, new_sides: list) -> None:
        self.side_lengths = new_sides

    def draw_polygon(self):
        for side in self.side_lengths:
            self.turtle.forward(side)
            self.turtle.right(360 / len(self.side_lengths))
        t.mainloop()


if __name__ == "__main__":
    hexagon = MyPolygon([100, 100, 100, 100, 100, 100])
    print(hexagon)
    print(hexagon.compute_perimeter())
    print(hexagon.get_number_of_edges())
    hexagon.draw_polygon()
