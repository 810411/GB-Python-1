import os
import shutil


# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

def create_dir(dir_name):
    try:
        dir_path = os.path.abspath(dir_name)
        os.mkdir(dir_path)
        print(os.path.abspath(dir_path), 'успешно создана')
    except FileExistsError as err:
        print('Такая директория уже существует:', err)
    except Exception as err:
        print('Ошибка:', err)


def delete_dir(dir_name):
    try:
        dir_path = os.path.abspath(dir_name)
        os.rmdir(dir_path)
        print(os.path.abspath(dir_path), 'успешно удалена')
    except FileNotFoundError as err:
        print('Файл или директория не найдены:', err)
    except Exception as err:
        print('Ошибка:', err)


if __name__ == "__main__":
    for i in range(1, 10):
        folder_name = 'dir_' + str(i)
        create_dir(folder_name)
    for i in range(1, 10):
        folder_name = 'dir_' + str(i)
        delete_dir(folder_name)


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def dir_info(current_dir):
    print('Текущая директория -', current_dir)
    print('Список папок текущей директории:')
    dir_count = 0
    for item in os.listdir(current_dir):
        if os.path.isdir(item):
            print(item)
            dir_count += 1
    if dir_count < 1:
        print('папки отсутствуют')


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def backup_file():
    this_file = __file__
    file_place_list = list(os.path.split(__file__))
    split_old_name = os.path.splitext(file_place_list[1])
    new_file_name = split_old_name[0] + '_copy' + split_old_name[1]
    new_file = os.path.join(file_place_list[0], new_file_name)
    try:
        shutil.copy(this_file, new_file)
    except Exception as err:
        print(err)
