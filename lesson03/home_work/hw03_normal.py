# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    fibonacci_list = [1]
    first_number, sec_number = 1, 1
    for i in range(2, m + 1):
        first_number, sec_number = sec_number, first_number + sec_number
        fibonacci_list.append(first_number)
    return list(filter(lambda x: x >= fibonacci_list[n - 1], fibonacci_list))


print(fibonacci(10, 13))


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def sort_to_max(origin_list):
    for i in range(0, len(origin_list)):
        for j in range(0, len(origin_list)):
            if origin_list[i] < origin_list[j]:
                origin_list[i], origin_list[j] = origin_list[j], origin_list[i]
    return origin_list


print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def my_filter(filter_func, iterator):
    return (iter for iter in iterator if filter_func(iter))


print(list(my_filter(filter_func=(lambda x: x > 5), iterator=[2, 10, -10, 8, 2, 0, 14])))


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def is_vertices(a1, a2, a3, a4):
    if abs(a3[0] - a2[0]) == abs(a4[0] - a1[0]) and abs(a2[1] - a1[1]) == abs(a3[1] - a4[1]):
        return True
    return False


# Задание - 5
# Вам даны 2 списка одинаковой длины, в первом списке имена людей, во втором зарплаты,
# вам необходимо получить на выходе словарь, где ключ - имя, значение - зарплата.
# Запишите результаты в файл salary.txt так, чтобы на каждой строке было 2 столбца,
# столбцы разделяются пробелом, тире, пробелом. в первом имя, во втором зарплата, например: Vasya - 5000
# После чего прочитайте файл, выведите построчно имя и зарплату минус 13% (налоги ведь),
# Есть условие, не отображать людей получающих более зарплату 500000, как именно
#  выполнить условие решать вам, можете не писать в файл
# можете не выводить, подумайте какой способ будет наиболее правильным и оптимальным,
#  если скажем эти файлы потом придется передавать.
# Так же при выводе имя должно быть полностью в верхнем регистре!
# Подумайте вспоминая урок, как это можно сделать максимально кратко, используя возможности языка Python.

names = ["Петр", "Василий", "Беркова", "Матвей", "Альберт"]
salaries = [22000, 18000, 666666, 42000, 17500]
sheet = dict(zip(names, salaries))

with open('files/sheet.txt', 'w', encoding='UTF-8') as sheet_file:
    for key, value in sheet.items():
        sheet_file.write(key + " - " + str(value) + '\n')

with open('files/sheet.txt', 'r', encoding='UTF-8') as sheet_file:
    for line in sheet_file:
        key, value = line.rstrip('\n').split(' - ')
        if int(value) < 500000:
            print(key.upper(), '-', int(value) * 0.87)
