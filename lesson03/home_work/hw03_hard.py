# Задание-1:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"
from pprint import pprint

hours = []
workers = []

with open('data/hours_of', 'r', encoding='utf8') as hours_file:
    for line in hours_file:
        hours.append(list(line.rstrip('\n').split()))

with open('data/workers', 'r', encoding='utf8') as workers_file:
    for line in workers_file:
        workers.append(list(line.rstrip('\n').split()))

hours.pop(0).sort()
workers.pop(0).sort()

for hour in hours:
    for worker in workers:
        salary, norm, fact = int(worker[2]), int(worker[4]), int(hour[2])
        if hour[0] == worker[0] and hour[1] == worker[1]:
            if fact < norm:
                worker[2] = round(salary / norm * fact)
            elif fact > norm:
                worker[2] = round(salary + 2 * (salary / norm * (fact - norm)))

pprint(workers)

# Задание - 2
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, persoтn2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.


player_name = input('Введите имя игрока: ')
enemy_name = input('Введите имя оппонента: ')

player = dict(name=player_name, health=100, damage=50)
enemy = dict(name=enemy_name, health=100, damage=50)


def attack(person1, person2):
    print(person1['name'], 'атакует', person2['name'])
    person2['health'] -= person1['damage']


# Задание - 3
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.

# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt
# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
# после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.


player['armor'] = 1.2
enemy['armor'] = 1.2


def damage(person1, person2):
    damage = int(person1['damage']) / float(person2['armor'])
    return round(damage)


def attack(person1, person2):
    damage_count = damage(person1, person2)
    health = int(person2['health']) - damage_count
    person2['health'] = health
    print(person1['name'], 'атакует', person2['name'], 'урон', damage_count)


with open('files/player.txt', 'w', encoding='UTF-8') as pf:
    for key, item in player.items():
        pf.write(str(key) + ' ' + str(item) + '\n')

with open('files/enemy.txt', 'w', encoding='UTF-8') as ef:
    for key, item in enemy.items():
        ef.write(str(key) + ' ' + str(item) + '\n')


def initializze(filename):
    with open('files/{}.txt'.format(filename), 'r', encoding='UTF-8') as pf:
        person_list = []
        for line in pf.readlines():
            person_list.append(line.rstrip("\n").split())
    person = dict(person_list)
    return person


def who_win(person1, person2):
    if int(person1['health']) == int(person2['health']):
        print("Ничья")
    elif int(person1['health']) > int(person2['health']):
        print("Победил", person1['name'], ", осталось здоровья:", person1['health'])
    else:
        print("Победил", person2['name'], ", осталось здоровья:", person2['health'])


print("Запуск игровой сессии")
player = initializze("player")
enemy = initializze("enemy")
while True:
    print(player)
    print(enemy)
    attack(player, enemy)
    if int(int(enemy['health'])) <= 0:
        break
    attack(enemy, player)
    if int(int(player['health'])) <= 0:
        break

who_win(player, enemy)
