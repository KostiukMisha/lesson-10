class Polygon:
    def __init__(self, num_sides):
        self.num_sides = num_sides

    def get_num_sides(self):
        return self.num_sides


class Rectangle(Polygon):
    def __init__(self, width, height):
        super().__init__(4)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


width = float(input("Введіть ширину прямокутника: "))
height = float(input("Введіть висоту прямокутника: "))

rect = Rectangle(width, height)

print(f"Кількість сторін: {rect.get_num_sides()}")
print(f"Площа прямокутника: {rect.area()}")
