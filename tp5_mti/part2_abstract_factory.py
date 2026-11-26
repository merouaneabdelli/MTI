class Shape:
    def draw(self):
        pass

    def erase(self):
        pass


class Circle(Shape):
    def draw(self):
        print("Circle.draw")

    def erase(self):
        print("Circle.erase")


class Square(Shape):
    def draw(self):
        print("Square.draw")

    def erase(self):
        print("Square.erase")


class Circle2D(Circle):
    def draw(self):
        print("Circle.draw2D")

    def erase(self):
        print("Circle.erase2D")


class Square2D(Square):
    def draw(self):
        print("Square.draw2D")

    def erase(self):
        print("Square.erase2D")


class Circle3D(Circle):
    def draw(self):
        print("Circle.draw3D")

    def erase(self):
        print("Circle.erase3D")


class Square3D(Square):
    def draw(self):
        print("Square.draw3D")

    def erase(self):
        print("Square.erase3D")


class ShapeFactory:

    @staticmethod
    def createShape(type):
        pass


class ShapeFactory2D(ShapeFactory):

    @staticmethod
    def createShape(type):

        if type == "Circle":
            return Circle2D()

        elif type == "Square":
            return Square2D()

        else:
            return None


class ShapeFactory3D(ShapeFactory):

    @staticmethod
    def createShape(type):

        if type == "Circle":
            return Circle3D()

        elif type == "Square":
            return Square3D()

        else:
            return None


if __name__ == "__main__":

    factory2D = ShapeFactory2D()
    factory3D = ShapeFactory3D()

    print("---- 2D Shapes ----")

    for type in ("Circle", "Square"):
        shape = factory2D.createShape(type)

        if shape is not None:
            shape.draw()
            shape.erase()

    print("---- 3D Shapes ----")

    for type in ("Circle", "Square"):
        shape = factory3D.createShape(type)

        if shape is not None:
            shape.draw()
            shape.erase()