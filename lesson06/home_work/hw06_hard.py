# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.

# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса, который наследуется от базового - Игрушка


class Toy:
    def __init__(self, name, color, toy_type):
        self.name = name
        self.color = color
        self.toy_type = toy_type

    def print_info(self):
        print('{}, {}, {}'.format(self.name, self.color, self.toy_type))


class ToyPet(Toy):
    pass


class ToyCartoon(Toy):
    pass


class ToyFactory:
    def purchase(self, name):
        print('Закуплены необходимые материалы для игрушки', name)

    def sewing(self, toy_type):
        print('Игрушка пошита по образцу типа:', toy_type)

    def painting(self, name, color):
        print('Игрушка {} раскрашена в {}'.format(name, color))

    def create_toy(self, name, color, toy_type):
        self.purchase(name)
        self.sewing(toy_type)
        self.painting(name, color)
        toy_type = toy_type.lower()
        if toy_type == 'животное':
            return ToyPet(name, color, toy_type)
        elif toy_type == 'персонаж':
            return ToyCartoon(name, color, toy_type)
        else:
            return Toy(name, color, toy_type)


factory = ToyFactory()
vaska = factory.create_toy('Васька', 'оранжевый', 'животное')
vaska.print_info()
mause = factory.create_toy('Микки', 'черно-белый', 'персонаж')
mause.print_info()
pillow = factory.create_toy('Мягкая', 'фиолетовый', 'подушка')
pillow.print_info()
