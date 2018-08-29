import os
import sys
import shutil

# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.
# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.
# P.S. По возможности, сделайте кросс-платформенную реализацию.

print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - создает копию указанного файла")
    print("rm <file_name> - удаляет указанный файл")
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную")
    print("ls - отображение полного пути текущей директории")


def make_dir():
    if not name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(name))
    except FileExistsError:
        print('директория {} уже существует'.format(name))


def change_dir():
    if not name:
        print("Необходимо указать имя директории вторым параметром")
        return
    if name.find('\\') == -1 or name.find('/') == -1:
        dir_path = os.path.abspath(name)
    else:
        dir_path = os.path.normpath(name)
    try:
        os.chdir(dir_path)
        print('текущая директория: ', os.getcwd())
    except FileNotFoundError:
        print('Папка {} не найдена'.format(name))
    except Exception as err:
        print(err)


def full_path():
    print(os.getcwd())


def ping():
    print("pong")


def backup_file():
    if not name:
        print("Необходимо указать имя файла вторым параметром")
        return
    split_file_name = os.path.splitext(name)
    new_file_name = split_file_name[0] + '_copy' + split_file_name[1]
    try:
        shutil.copy(name, new_file_name)
        print('файл {} скопирован в {}'.format(name, new_file_name))
    except FileNotFoundError:
        print('Файл {} не найден'.format(name))
    except Exception as err:
        print(err)


def remove_file():
    if not name:
        print("Необходимо указать имя файла вторым параметром")
        return
    print('Вы уверены что хотите удалить файл {}? Введите "Y" для подтверждения'.format(name))
    choose = input().upper()
    if choose != 'Y':
        return
    try:
        os.remove(os.path.join(os.getcwd(), name))
        print('файл {} удален'.format(name))
    except FileNotFoundError:
        print('Файл {} не найден'.format(name))
    except Exception as err:
        print(err)


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": backup_file,
    "rm": remove_file,
    "cd": change_dir,
    "ls": full_path
}

try:
    name = sys.argv[2]
except IndexError:
    name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None

if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
