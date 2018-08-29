# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)
# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.


class Car:
    def __init__(self, name: str, max_speed: int, transmission: bool, body_type: str, is_police=False):
        self.name = name
        self._color = 'white'
        self._max_speed = max_speed
        self._transmission = transmission
        self._body_type = body_type
        self._is_police = is_police

    def go(self):
        return self.name + ' is driven'

    def acceleration(self, speed):
        if speed >= self._max_speed:
            speed = self._max_speed
        return self.go() + ' with speed ' + speed + 'mph'

    def stop(self):
        return self.name + ' is parking'

    def turn(self, direction):
        return self.name + ' turns ' + direction

    def transmission_type(self):
        if self._transmission:
            return 'automatic'
        else:
            return 'manual'

    def is_police(self):
        return 'Polce car' if self._is_police else None

    def get_body_type(self):
        return self._body_type

    def set_color(self, color):
        self._color = color

    def get_color(self):
        return self._color


class TownCar(Car):
    pass


class PoliceCar(Car):
    def siren_on(self):
        return 'wooow woooow'


class WorkingCar(Car):
    def __init__(self, name, max_speed, transmission, body_type, carrying):
        super().__init__(name, max_speed, transmission, body_type)
        self.carrying = carrying

    def broken(self):
        return 'lol!'


class SportCar(Car):
    def __init__(self, name, max_speed, transmission, body_type, nitro_factor: float):
        super().__init__(name, max_speed, transmission, body_type)
        self._nitro_factor = nitro_factor

    def acceleration(self, speed):
        if speed >= self._max_speed:
            speed = self._max_speed
        return self.go() + ' with speed ' + str(round(speed * self._nitro_factor)) + 'mph'


car1 = PoliceCar('Ford', 160, False, 'sedan', True)
car1.set_color('black')
car2 = WorkingCar('Peugeot', 100, True, 'wagon', 300)
car3 = SportCar('Ferrari', 200, False, 'coupe', 1.2)
car3.set_color('red')
car4 = TownCar('Toyota', 140, True, 'sedan')


def print_car_info(car):
    print('{}, {}, {}.'.format(car.name, car.get_body_type(), car.get_color()))


print_car_info(car1)
print_car_info(car2)
print_car_info(car3)
print_car_info(car4)

for i in (1, 2, 3, 'Start'):
    print(i)

print('{}. {}. {}.'.format(car2.go(), car3.go(), car4.go()))
print(car2.broken(), car2.stop())
print('{} {}, {}'.format(car1.is_police(), car1.go(), car1.siren_on()))
print(car4.turn('into the yard '))
print(car3.acceleration(300))
