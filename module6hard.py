from math import pi, sqrt


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
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if all(isinstance(value, int) and 0 <= value <= 255 for value in (r, g, b)):
            return r,g,b
        else:
            return self.__color

    def set_color(self, r, g, b):
        new_color = self.__is_valid_color(r, g, b)
        self.__color = list(new_color)
        return self.__color

    def __is_valid_sides(self, *__sides):
        prow1 = all(isinstance(side, int) and side > 0 for side in __sides)
        if isinstance(self, Cube):
            prow2 = len(__sides) == 1
        else:
            prow2 = len(__sides) == self.sides_count
        return prow1 and prow2


    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)


    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            if isinstance(self, Cube):
                self.__sides = list(new_sides) * self.sides_count
            else:
                self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, __color, *__sides):
        super().__init__(__color, __sides)
        self.__radius = self.__calculate_radius()

    def __calculate_radius(self):
        return self.get_sides()[0] / (2 * pi)

    def get_radius(self):
        return self.__radius

    def get_square(self):
        return pi * (self.__radius ** 2)

class Triangle(Figure):
    sides_count = 3

    def __init__(self, __color, *__sides):
        super().__init__(__color, __sides)
        self.__height = self.__calculate_height()

    def __calculate_height(self):
        p = sum(self.get_sides()) / 2
        osn = self.get_sides()[0]
        return (2 * sqrt(p * (p - osn) * (p - self.get_sides()[1]) * (p - self.get_sides()[2]))) / osn

    def get_square(self):
        return (self.__calculate_height() * self.get_sides()[0]) / 2


class Cube(Figure):
    sides_count = 12

    def __init__(self, __color, *__sides):
        super().__init__(__color, __sides)

    def get_volume(self):
        return super().get_sides()[0] ** 2 * 6

circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
triangle1 = Triangle((155, 56, 30), 8, 3, 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(77, 500, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))
#
# # Проверка объёма (куба):
print(cube1.get_volume())


# площадь
print(circle1.get_square())
print(triangle1.get_square())

