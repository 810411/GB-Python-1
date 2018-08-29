import random

# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

initial_list = [1, 2, 4, 0]
result_list = [item ** 2 for item in initial_list]
print(result_list)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

first_list = ['apple', 'orange', 'mango', 'kiwi']
second_list = ['mango', 'pineapple', 'lemon', 'apple', 'mandarin']
third_list = [item for item in first_list if second_list.count(item) > 0]
print(third_list)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

rand_num_list = [random.randint(-100, 100) for _ in range(100)]
mod_rand_num_list = [item for item in rand_num_list if item >= 0 and item % 3 == 0 and item % 4 != 0]
print(mod_rand_num_list)

