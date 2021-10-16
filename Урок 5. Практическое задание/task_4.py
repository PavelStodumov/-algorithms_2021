"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from timeit import timeit

my_dict = {i: i**2 for i in range(10000)}
my_ord_dict = {i: i**2 for i in range(10000)}

def get_elems(n, m, obj):
    return [obj[i] for i in range(n, m)]

def add_elems(n, obj):
    for i in range(n):
        obj[f'{i}'] = i / 2
    return obj




print('Создание dict: ', timeit('my_dict', globals=globals()))
print('Создание orderdict', timeit('my_ord_dict', globals=globals()))

print('Извлечение массива значений dict: ', timeit('get_elems(250, 750, my_dict)', globals=globals(), number=1000))
print('Извлечение массива значений orderdict', timeit('get_elems(250, 750, my_ord_dict)', globals=globals(), number=1000))

print('Добавление элементов dict: ', timeit('add_elems(500, my_dict)', globals=globals(), number=1000))
print('Добавление элементов orderdict', timeit('add_elems(500, my_ord_dict)', globals=globals(), number=1000))

'''Отличий в плане скорости не обнаружил'''
