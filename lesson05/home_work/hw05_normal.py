import os
import sys
import lesson05.home_work.hw05_easy as my_mod


# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py


def start_magic(choose):
    if choose == 0:
        sys.exit()
    if choose == 1:
        try:
            dir_name = input('Введите путь до папки используя разделитель "/" или "\\": ')
            dir_name = os.path.normpath(dir_name)
            os.chdir(dir_name)
            print('Текущая директория:', os.getcwd())
        except FileNotFoundError as err:
            print('Файл или директория не найдены:', err)
        except Exception as err:
            print(err)
    if choose == 2:
        current_dir = os.getcwd()
        my_mod.dir_info(current_dir)
    if choose == 3:
        dir_name = input('Введите имя папки: ')
        my_mod.create_dir(dir_name)
    if choose == 4:
        dir_name = input('Введите имя папки: ')
        my_mod.delete_dir(dir_name)


while True:
    try:
        print('Выберите действие:')
        print('1. Перейти в папку')
        print('2. Просмотреть содержимое текущей папки')
        print('3. Создать папку')
        print('4. Удалить папку')
        print('0. Выход')
        user_choose = int(input())
        start_magic(user_choose)
    except ValueError as err:
        print('Для выбора действия введите соответствующий номер')
    except Exception as err:
        print(err)
