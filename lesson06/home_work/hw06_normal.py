# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.

from random import randint


class Person:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.damage = 50

    def _damage_via_armor(self, person1, person2):
        damage = person1.damage / person2.armor
        return round(damage)

    def attack(self, person1, person2):
        damage_count = self._damage_via_armor(person1, person2)
        person2.health = person2.health - damage_count
        print(self.battle_cry(), person1.name, 'атакует', person2.name, 'урон', damage_count)

    def print_info(self):
        print('Боец: {} со здоровьем: {}'.format(self.name, self.health))

    def battle_cry(self):
        pass


class Player(Person):
    def __init__(self, name):
        super().__init__(name)
        self.armor = 2
        self.damage = 60

    def battle_cry(self):
        return 'За императора!'


class Enemy(Person):
    def __init__(self, name):
        super().__init__(name)
        self.armor = randint(100, 200) / 100
        self.damage = randint(20, 40)

    def battle_cry(self):
        return 'Waaagh!'


class GameSession:
    def __init__(self, player, *enemy_list):
        self.player = player
        self.enemy_list = enemy_list

    def win_call(self, winner):
        print("Победил {}, осталось здоровья {}".format(winner.name, winner.health))

    def start_session(self):
        print('Да начнется битва!')
        for enemy in self.enemy_list:
            while True:
                self.player.print_info()
                enemy.print_info()
                self.player.attack(self.player, enemy)
                if enemy.health <= 0:
                    self.win_call(self.player)
                    break
                enemy.battle_cry()
                enemy.attack(enemy, self.player)
                if self.player.health <= 0:
                    self.win_call(enemy)
                    break
        print()


player = Player('player')
enemy1 = Enemy('enemy1')
enemy2 = Enemy('enemy2')
enemy3 = Enemy('enemy3')

session1 = GameSession(player, enemy1)
session2 = GameSession(player, enemy1, enemy2, enemy3)

session1.start_session()
session2.start_session()
