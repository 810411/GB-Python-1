"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11      
      16 49    55 88    77    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""

import random


class Card:
    """
    Класс шаблон для создания объектов карточек
    """

    def __init__(self, name: str, numbers_lst):
        self._name = name[0:24] if len(name) > 24 else name
        self._numbers_list = numbers_lst
        self._numbers = self._fill_card()
        self._cross = 0

    def _fill_card(self):
        """
        Метод заполняющий карточки цифрами при инициализации объекта карточки
        """
        random_list = []
        while len(random_list) <= 27:
            n = random.choice(self._numbers_list)
            if n not in random_list:
                random_list.append(n)
        random_list.sort()
        dct = dict(zip(range(27), random_list))
        for i in range(0, 3):
            for_delete = random.sample(range(i, len(dct), 3), 4)
            for j in range(i, len(dct), 3):
                if j in for_delete:
                    dct[j] = ' '
        return dct

    def validate_number(self, number):
        """
        Проверяет наличие переданной цифры в карточке
        """
        if number in self._numbers.values():
            return True
        return False

    def cross_number(self, number):
        """
        Зачеркивает переданную цифру совпадающюю с цифрой карточки
        """
        for key in self._numbers.keys():
            if self._numbers[key] == number:
                self._numbers[key] = 'XX'
                self._cross += 1

    def get_cross(self):
        return self._cross

    def print_card(self):
        """
        Выводит содержимое карточки на экран
        """
        name = ' ' + self._name + ' '
        print('{:-^26}'.format(name))
        for i in range(0, 3):
            for j in range(i, len(self._numbers), 3):
                print('{: >2} '.format(self._numbers[j]), end='')
            print()
        print('-' * 26)


class Game:
    """
    Класс для создания объекта игровой сессии
    """

    def __init__(self):
        """
        Инициализация игровой сессии при которой создаются два объекта типа Card
        """
        self._bag = list(range(1, 91))
        self._player_card = Card('Ваша карточка', self._bag)
        self._ai_card = Card('Карточка компьютера', self._bag)
        self._notice = ['Вы проиграли!', 'Поздравляем! Вы выиграли!', 'Нажмите "y" или "n"']

    def game(self):
        """
        Метод в котором происходит игровое взаимодействие
        """
        while self._bag:
            random.shuffle(self._bag)
            keg = self._bag.pop()
            print('Зачеркнуто номеров: {} - {}'.format(self._player_card.get_cross(), self._ai_card.get_cross()))
            print('Новый бочонок: {} (осталось {})'.format(keg, len(self._bag)))
            self._player_card.print_card()
            self._ai_card.print_card()
            while True:
                choose = input('Зачеркнуть цифру? (y/n)').lower()
                if choose != 'y' and choose != 'n':
                    print(self._notice[2])
                    continue
                break
            if choose == 'y':
                if self._player_card.validate_number(keg):
                    self._player_card.cross_number(keg)
                else:
                    print(self._notice[0])
                    break
            else:
                if self._player_card.validate_number(keg):
                    print(self._notice[0])
                    break
            if self._ai_card.validate_number(keg):
                self._ai_card.cross_number(keg)
            if self._player_card.get_cross() == 15:
                print(self._notice[1])
                self._player_card.print_card()
                break
            if self._ai_card.get_cross() == 15:
                print(self._notice[0])
                break
            print()


game_session = Game()
game_session.game()
