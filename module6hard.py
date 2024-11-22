class Figure:
    sides_count = 0

    def __init__(self, __color: tuple, __sides: tuple):
        if self.__is_valid_sides(*__sides):
            if isinstance(self, Cube):
                self.__sides = list(__sides) * self.sides_count
            else:
                self.__sides = list(__sides)
        else:
            self.__sides = [1] * self.sides_count
        self.__color = list(__color) if self.__is_valid_color(*__color) else [0, 0, 0]
        self.filled = True

    def get_color(self):
        print(self.color)

    def __is_valid_color(self, color_):
        a = list(color_)
        if 0 <= a[0] <= 255 and 0 <= a[1] <= 255 and 0 <= a[2] <= 255:
            return True

    def set_color(self, color_: tuple):
        if Figure.__is_valid_color(self, color_):
            self.color = list(color_)

    def __is_valid_sides(self):
        if len(Figure.get_sides(self)) == sides_count:
            for a in Figure.get_sides(self):
                if a < 0:
                    return False
        return True
        #if self.sides

    def get_sides(self):
        if sides_count == len(Figure.get_sides(self)):
            return self.sides
        else:
            return [1]*sides_count

    def __len__(self):
        return sum(self.sides)


class Circle(Figure):
    sides_count = 1
    #_radius = len()

class Triangle(Figure):
    sides_count = 3
    st = Figure(self.sides)
    perimetr = sum(st)
    __height = 2 / (st[0]*(perimetr*(perimetr-st[0])*(perimetr-st[1])*(perimetr-st[2]))**0.5)

    def get_square(self):
        return Figure(self.sides)[0] * Triangle.__height


class Cube(Figure):
    sides_count = 12

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится

print(circle1.get_color())


