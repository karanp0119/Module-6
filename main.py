def main():
    class Rectangle:
        def __init__(self, posn, w, h):
            self.corner = posn
            self.width = w
            self.height = h

    class Cords:
        def __init__(self, x, y):
            self.x = x
            self.y = y

    def create_rectangle(x, y, w, h):
        return Rectangle(Cords(x, y), w, h)

    def str_rectangle(r):
        return "({0}, {1}, {2},{3})".format(r.corner.x, r.corner.y, r.width, r.height)

    def shift_rectangle(r, dx, dy):
        r.corner = Cords(dx, dy)

    def offset_rectangle(r1, dx, dy):
        return Rectangle(Cords(r1.corner.x + dx, r1.corner.y + dy), r1.width, r1.height)

    r1 = create_rectangle(10, 20, 30, 40)
    print(str_rectangle(r1))

    shift_rectangle(r1, -10, -20)
    print(str_rectangle(r1))

    r2 = offset_rectangle(r1, 100, 100)
    print(str_rectangle(r1))
    print(str_rectangle(r2))


if __name__ == "__main__":
    main()
