#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------
# Модули:

# Парсер аргументов командной строки:
import argparse
# Переменные операционной системы:
import os
# Регулярные выражения:
import re

# Автоматизацией не пренебрегай:
# _-Смешивание лапши в миске (килограмм)..... | 19
# _-Смешивание риса в миске (килограмм)...... | 45
# _-Смешивание салата в миске (килограмм).... | 51
# Преобразуем вывод в новые элементы словаря:
# xclip -o | sed "s@# @@" | sed "s@\.* | .*@@gi" | sed "s@^@metadict_detail['@" | sed "s@\$@'] = {@" | sed "s@\$@\n        }\n@"
# Или так, сразу дополняя:
# xclip -o | sed "s@# @@" | sed "s@\.* | .*@@gi" | sed "s@\(.*\)@metadict_army['\1'] = {\n        '\1':1,\n        }\n@"
# Строки из вывод в строки словаря:
# xclip -o | xclip -o | sed "s@# @@" | sed "s@\.* | .*@@gi" | sed "s@\(.*\)@        '\1':1,@gi"

#-------------------------------------------------------------------------
# Опции:

# Каталог словарей:
METADICT_DIR = 'dict'
# Объект для исследования по умолчанию:
SQUAD = ''
# Число однотипных объектов для исследования:
NUMBER = 1
# Глубина исследования:
DEPTH = 99

#-------------------------------------------------------------------------
# Аргументы командной строки:

def create_parser():
    """Список доступных параметров скрипта."""
    parser = argparse.ArgumentParser()
    parser.add_argument('squad',
                        nargs='*',
                        help='Название отряда (в "кавычках")'
                        )
    parser.add_argument('-D', '--directory',
                        action='store', dest='dir', type=str,
                        help='Каталог словарей (путь)'
                        )
    parser.add_argument('-d', '--depth',
                        action='store', dest='depth', type=int,
                        help='Глубина исследования (0-999)'
                        )
    parser.add_argument('-n', '--number',
                        action='store', dest='number', type=float,
                        help='Доля отряда, либо число отрядов (0.001-999)'
                        )
    parser.add_argument('-e', '--except',
                        action='store', dest='exc', type=str, nargs='*',
                        help='Искать в составе отряда (строка в "кавычках")'
                        )
    parser.add_argument('-s', '--short',
                        action='store_true', default='False',
                        help='Краткий вывод, обобщение, расчёты'
                        )
    parser.add_argument('-m', '--model',
                        action='store_true', default='False',
                        help='Моделирование, затраты времени'
                        )
    return parser

#-------------------------------------------------------------------------
# Функции:

def metadict_path (metadict_dir):
    """Возвращает абсолютный путь к каталогу словарей."""
    # Получаем абсолютный путь к каталогу скрипта:
    script_path = os.path.dirname(os.path.abspath(__file__))
    # Добавляем к пути каталог словарей:
    metadict_path = script_path + '/' + metadict_dir
    return metadict_path

def find_files (directory):
    """Возвращает список путей ко всем файлам каталога, включая подкаталоги."""
    path_f = []
    for d, dirs, files in os.walk(directory):
        for f in files:
                # Формирование адреса:
                path = os.path.join(d,f)
                # Добавление адреса в список:
                path_f.append(path)
    return path_f

def key_search (search_string, dict):
    """Поиск нужного объекта в словаре, выбор по списку совпадений."""
    # Создаётся регистронезависимая поисковая строка:
    p = re.compile(search_string, re.I)
    # Создаём словарь совпадений:
    dict_found = {}
    counter = 0
    # Поиск в словаре:
    for line in sorted(dict.keys()):
        if p.findall(line):
            dict_found[counter] = line
            search_string = line
            counter = counter + 1
    # Если искомое не найдено, тогда выход:
    if not dict_found:
        print('---Совпадений не найдено')
        exit(0)
    # Если найден один варинт, тогда его и выбираем:
    elif len(dict_found) == 1:
        squad = dict_found[0]
    # Если несколько совпадений, тогда выбор по номеру:
    else:
        for key in dict_found:
            print(key,dict_found[key])
        string_number = input('---Найдено несколько совпадений (введите номер): ')
        search_string = dict_found[int(string_number)]
        squad = search_string
        print('-----------------------------------------------------')
    return squad

def bfd(vertex, number, dict_crew, metadict_army):
    """Обработка иерархической базы данных, функция обхода в ширину."""
    #print ('    vertex:', vertex, number)
    # Проверка, является ли объект составным:
    if vertex in metadict_army:
        # Определяется состав объекта:
        for key,value in sorted(metadict_army[vertex].items()):
            #print ('        key:', key, value)
            if vertex in dict_crew:
                value = value * dict_crew[vertex]
            else:
                value = value * number
            # Если объект уже есть в рабочем словаре, прибавить:
            if key in dict_crew:
                dict_crew[key] = dict_crew[key] + value
            # Иначе создать новый объект:
            else:
                dict_crew[key] = value
    # Если объект цельный:
    else:
        # Проверка, есть ли такие объекты в рабочем словаре:
        if vertex in dict_crew:
            # Если да, суммировать:
            dict_crew[vertex] = dict_crew[vertex] + number
        else:
            dict_crew[vertex] = number

#-------------------------------------------------------------------------
# Обработка аргументов командной строки:

# Создаётся список аргументов скрипта:
parser = create_parser()
namespace = parser.parse_args()

# Проверка, указана ли ссылка на каталог словарей (ключ -D --directory):
if namespace.dir:
    dir_path = os.path.expanduser(namespace.dir)
    dicts_list = find_files(dir_path)
else:
    dicts_list = find_files(metadict_path(METADICT_DIR))

# Загрузка словарей в базу данных:
metadict_army = {}
metadict_detail = {}
metadict_model = {}
for file_path in dicts_list:
    with open(file_path) as f:
        code = compile(f.read(), file_path, 'exec')
        exec(code, globals(), locals())

# Проверка, выбран ли словарь деталей (ключ -s --short):
if namespace.short is True:
    # Объединяем словари
    metadict_army.update(metadict_detail)

# Проверка, выбран ли словарь модели (ключ -m --model):
if namespace.model is True:
    # Объединяем словари
    metadict_army.update(metadict_model)

# Проверка, введено ли название отряда:
if namespace.squad:
    squad = ' '.join(namespace.squad)
else:
    # Если нет, берём стандартный:
    squad = SQUAD

# Проверка, указано ли число расчётных объектов:
if namespace.number is not None:
    obj_number = namespace.number
else:
    # Если нет, берём из опций:
    obj_number = NUMBER

# Если название неточное, срабатывает встроенный поисковик:
if squad not in metadict_army.keys():
    squad = key_search(squad, metadict_army)
    print('Выбрано:', squad, round(obj_number))

# Исключаем (выделяем) указанный объект из словаря:
if namespace.exc:
    squad_except = ' '.join(namespace.exc)
    # Если название неточное, срабатывает встроенный поисковик:
    if squad_except not in metadict_army.keys():
        print('-----------------------------------------------------')
        print('---Число каких объектов вычисляем?')
        squad_except = key_search(squad_except, metadict_army)
else:
    squad_except = None

# Проверка, указана ли глубина исследования:
if namespace.depth != None:
    depth = namespace.depth
else:
    # Если нет, мспользовать стандартную:
    depth = DEPTH

#-------------------------------------------------------------------------
# Исполняемый код:

# Рабочий словарь:
dict_crew = {}

# Многоуровневый обход в ширину:
if depth == 0:
    for key,value in sorted(metadict_army[squad].items()):
        key = key * obj_number
        dict_crew[key] = value
else:
    cycles = depth - 1
    # Формируется временный словарь
    for key,value in sorted(metadict_army[squad].items()):
        value = value * obj_number
        # Первый уровень исследования
        #print ('-----------------')
        #print ('cycle:',cycles)
        bfd(key, value, dict_crew, metadict_army)
        #print ('    dict:', dict_crew)
    # Цикл исследования временного словаря
    while cycles > 0:
        #print ('-----------------')
        #print ('cycle:',depth)
        for key,value in sorted(dict_crew.items()):
            if key in metadict_army and squad_except != key:
                # Функция извлекает состав объекта:
                bfd(key, value, dict_crew, metadict_army)
                # Удаляется обработанный объект из словаря:
                dict_crew.pop(key)
                #print ('    dict:', dict_crew)
        cycles -= 1
        depth -= 1


# Ищем самый длинный ключ в словаре:
longest_key=max(map(len, dict_crew))

# Вывод данных:
if namespace.exc:
    value = dict_crew.pop(squad_except, 0)
    #print(squad_except, round(value))
    print ('{0:.<{width}} | {1:0,}'.format(squad_except, round(value), width=longest_key))
else:
    for key,value in sorted(dict_crew.items()):
        print ('{0:.<{width}} | {1:0,}'.format(key, round(value), width=longest_key))
        #print(key, round(value))
        #print(key)
