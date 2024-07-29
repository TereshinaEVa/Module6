class Vehicle:
    __COLOR_VARIANTS = ['BLACK', 'WHITE', 'RED', 'GOLD', 'SILVER', 'BLUE']
    def __init__(self, owner: str, model: str, engine_power: int, color: str):
        self.owner = owner
        self.__model = model
        self.__enqine_power = engine_power
        self.__color = color

    def get_model(self):
        print(f'Модель: {self.__model}')

    def get_horsepower(self):
        print(f'Мощность двигателя: {self.__enqine_power}')

    def get_color(self):
        print(f'Цвет: {self.__color}')

    def print_info(self):
        Vehicle.get_model(self)
        Vehicle.get_horsepower(self)
        Vehicle.get_color(self)
        print(f'Владелец: {self.owner}')

    def set_color(self,new_color: str):
        if new_color.upper() in Vehicle.__COLOR_VARIANTS:
            self.color = new_color.upper()
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Ivan', 'UAZ', 120, 'Green')

vehicle1.print_info()

vehicle1.set_color('yellow')
vehicle1.set_color('Black')
vehicle1.owner = ('Petrukha')

vehicle1.print_info()