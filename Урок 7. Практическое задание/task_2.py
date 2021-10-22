"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Хотя в примерах к уроку уже есть вариант реализации слияния,
попробуйте предложить другой (придумать или найти).

И попытаться сделать замеры на массивах разной длины: 10, 100, 1000, ...

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
from random import uniform
from timeit import timeit




def merge(ls1, ls2): # функция слияния двух списков с сортировкой
    sort_ls = []
    index_ls1, index_ls2 = 0, 0
    while index_ls1 < len(ls1) and index_ls2 < len(ls2):
        if ls1[index_ls1] < ls2[index_ls2]:
            sort_ls += [ls1[index_ls1]]
            index_ls1 += 1
        else:
            sort_ls += [ls2[index_ls2]]
            index_ls2 += 1

    while index_ls1 < len(ls1):
        sort_ls += [ls1[index_ls1]]
        index_ls1 += 1

    while index_ls2 < len(ls2):
        sort_ls += [ls2[index_ls2]]
        index_ls2 += 1

    return sort_ls

def my_sort(ls):
    ls = list(map(lambda x: [x], ls)) # делим массим на подмассивы длинной 1
    while len(ls) > 1:  # пока длинна массива больше 1
        ls.append(merge(ls.pop(0), ls.pop(0))) # берём первые два элемента, сливаем их и помещаем в конец
    return ls[0] # т.к. массив получился двумерный, выводим 0 элемент

my_list = [uniform(0, 50) for _ in range(10)]

print(my_sort(my_list[:]))
print(my_list)

print('время сортировки моей функцией массива из 10 элементов', timeit('my_sort([uniform(0, 50) for _ in range(10)])', globals=globals(), number=10000))
print('время сортировки функцией sorted() массива из 10 элементов', timeit('sorted([uniform(0, 50) for _ in range(10)])', globals=globals(), number=10000), end='\n\n')

print('время сортировки моей функцией массива из 100 элементов', timeit('my_sort([uniform(0, 50) for _ in range(100)])', globals=globals(), number=10000))
print('время сортировки функцией sorted() массива из 100 элементов', timeit('sorted([uniform(0, 50) for _ in range(100)])', globals=globals(), number=10000), end='\n\n')

print('время сортировки моей функцией массива из 1000 элементов', timeit('my_sort([uniform(0, 50) for _ in range(1000)])', globals=globals(), number=1000))
print('время сортировки функцией sorted() массива из 1000 элементов', timeit('sorted([uniform(0, 50) for _ in range(1000)])', globals=globals(), number=1000), end='\n\n')

'''Моя функция работает очень медленно, думаю из за pop(0) теряется много времени(пересчёт индексов). Зато решение моё.
Концепцию сортировки слиянием думаю я понял'''