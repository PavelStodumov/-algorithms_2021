"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры.

Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание не принимается

И прошу вас обратить внимание, что то, что часто ошибочно называют генераторами списков,
на самом деле к генераторам отношения не имеет. Это называется "списковое включение" - list comprehension.
"""
from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0: # сразу не понравилось что каждый элемент вычисляется по индексу для проверки чётности
            new_arr.append(i)
    return new_arr


def func_2(nums):
    new_arr = []
    count = 0 # переменная-счетчик будет выступать в качестве индексов
    for i in nums: # циклом перебираем элементы, а не индексы, как в исходнике
        if i % 2 == 0: # теперь для проверки на чётность не вычисляется элемент по индексу
            new_arr.append(count)
        count += 1
    return new_arr


def func_3(nums):  # list comprehension дал прирост скорости
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


def func_4(nums):  # не создавая новый список выводим сразу последовательность ещё не большой прирост
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]  # хотя показания неоднозначны


my_list = [i for i in range(100)]

print(timeit('func_1(my_list)', globals=globals(), number=500000), ' время для func_1')
print(timeit('func_2(my_list)', globals=globals(), number=500000), ' время для func_2')
print(timeit('func_3(my_list)', globals=globals(), number=500000), ' время для func_3')
print(timeit('func_4(my_list)', globals=globals(), number=500000), ' время для func_4')

'''Результаты замеров всё таки не однозначны'''