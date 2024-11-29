class Vehicle: #  это любой транспорт
    # атрибут класса:
    __COLOR_VARIANTS = ['red', 'blue', 'black', 'yellow', 'green'] # в который записан список допустимых
                        # цветов для окрашивания. (Цвета написать свои)

    # атрибуты объекта:
    owner = str #  владелец транспорта. (владелец может меняться)
    __model = str # модель (марка) транспорта. (мы не можем менять название модели)
    __engine_power = int # мощность двигателя. (мы не можем менять мощность двигателя самостоятельно)
    __color = str # название цвета. (мы не можем менять цвет автомобиля своими руками)

    def __init__(self, owner = str, __model = str, __color = str, __engine_power = int):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    # следующие методы:
    def get_model(self): # возвращает строку: "Модель: <название модели транспорта>"
        return f'Модель: {self.__model}'

    def get_horsepower(self): # возвращает строку: "Мощность двигателя: <мощность>"
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self): # возвращает строку: "Цвет: <цвет транспорта>"
        return f'Цвет: {self.__color}'

    def print_info(self): # распечатывает результаты методов (в том же порядке):
        print(self.get_model()) # get_model, get_horsepower, get_color;
        print(self.get_horsepower())# а так же владельца в конце в формате "Владелец: <имя>"
        print(self.get_color())
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color = str): # принимает аргумент new_color(str),
        if new_color.lower() in self.__COLOR_VARIANTS: # меняет цвет __color на new_color,
            self.__color = new_color  # если он есть в списке __COLOR_VARIANTS
        else:
            print(f'Нельзя сменить цвет на {new_color}')

    # Взаимосвязь методов и скрытых атрибутов:
    # Методы get_model, get_horsepower, get_color находятся в одном классе с соответствующими им атрибутами:
    # __model, __engine_power, __color. Поэтому атрибуты будут доступны для методов.
    # Атрибут класса __COLOR_VARIANTS можно получить обращаясь к нему через объект(self).
    # Проверка в __COLOR_VARIANTS происходит не учитывая регистр ('BLACK' ~ 'black').


class Sedan(Vehicle): # наследник класса Vehicle
    __PASSENGERS_LIMIT = 5 # (в седан может поместиться только 5 пассажиров)


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()

