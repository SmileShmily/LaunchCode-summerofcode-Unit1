'''In games, we often put a rectangular “bounding box” around our sprites in the game.
 We can then do collision detection between, say, bombs and spaceships, by comparing whether their rectangles overlap anywhere.

Write a function to determine whether two rectangles collide. Hint: this might be quite a tough exercise!
 Think carefully about all the cases before you code.
'''


def collides_with(self):
    """In games, we often put a rectangular “bounding box” around our sprites
    in the game. We can then do collision detection between, say, bombs and
    spaceships, by comparing whether their rectangles overlap anywhere.
    Write a function to determine whether two rectangles collide. Hint: this
    might be quite a tough exercise! Think carefully about all the cases
    before you code."""
    # TODO
    pass


if __name__ == "__main__":
    # Points
    p = Point(5, 5)
    q = Point(6, -2)
    r = Point(2, -4)
    center_circle(p, q, r)

    # Fractions
    myfraction = Fraction(12, 16)
    print(myfraction.get_num())
    print(myfraction.get_den())
    print(myfraction.gcd(4, 98))
    myfraction.simplify()
    f1 = Fraction(1, 2)
    f2 = Fraction(1, 4)
    f4 = f1 * f2

    # Rectangle
    R = Rectangle(Point(4, 5), 10, 5)
    assert R.area() == 50
    assert R.perimeter() == 30
    R.transpose()
    print(R.diagonal())

    r = Rectangle(Point(0, 0), 10, 5)
    assert r.contains(Point(0, 0)) == True
    assert r.contains(Point(3, 3)) == True
    assert r.contains(Point(3, 7)) == False
    assert r.contains(Point(3, 5)) == False
    assert r.contains(Point(3, 4.99999)) == True
    assert r.contains(Point(-3, -3)) == False


