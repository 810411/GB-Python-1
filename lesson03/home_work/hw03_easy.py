# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    number_split = str(number).split('.')
    remainder = int(number_split[1])
    round_cycles = len(number_split[1]) - ndigits
    if round_cycles <= 0:
        return number
    else:
        while (round_cycles):
            last_remainder_item = remainder % 10
            if last_remainder_item >= 5:
                remainder = (remainder // 10) + 1
            else:
                remainder = remainder // 10
            round_cycles -= 1
        number = int(number_split[0]) + remainder / (10 ** ndigits)
        return number


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))
print(my_round(2.1234567, 3))
print(my_round(2.1234567, 1))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    if len(str(ticket_number)) != 6:
        return 'Билет некорректный'
    left_item = [int(char) for char in str(ticket_number // 1000)]
    right_item = [int(char) for char in str(ticket_number % 1000)]
    if sum(left_item) == sum(right_item):
        return 'Билет счастливый'
    else:
        return 'Билет обычный'


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
print(lucky_ticket(123456))


# Задание - 3
# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"

def person(name, age, city):
    return '{}, {} год(а), проживает в городе {}'.format(name, age, city)


print(person('Василий', '21', 'Москва'))


# Задание - 4
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них

def max_of_three(one, two, three):
    if one > two and one > three:
        return one
    elif two > one and two > three:
        return two
    else:
        return three


def max_of_three2(one, two, three):
    return max(one, two, three)


print(max_of_three(1, 2, 3), max_of_three(10, 5, 7), max_of_three(4, 9, 2))
print(max_of_three2(1, 2, 3), max_of_three2(10, 5, 7), max_of_three2(4, 9, 2))


# Задание - 5
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов

def max_of_str(*args):
    return str(max(args, key=len))


print(max_of_str("Создайте функцию", "принимающую неограниченное количество", "строковых аргументов"))
