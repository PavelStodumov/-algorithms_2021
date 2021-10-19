"""
Задание 1.

Выполните профилирование памяти в скриптах.
Проанализируйте результат и определите программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять только домашние задания с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""
##############################################################################################
import memory_profiler
import collections
from timeit import timeit, default_timer


# Создать список, состоящий из кубов нечётных чисел от 1 до 100000(прибавил пару нулей для наглядности):
# a.Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.

def get_mem_time(func):  # декоратор для замера памяти
    def wrapper(*args):
        m_start = memory_profiler.memory_usage()[0]
        t_start = default_timer()
        r = func(*args)
        print(f'потреблено: {memory_profiler.memory_usage()[0] - m_start} памяти')
        print(f'затрачено: {default_timer() - t_start} времени')
        return r

    return wrapper


@get_mem_time
def func():
    numbers = [number ** 3 for number in range(1, 1000000, 2)]

    def get_sum():
        total = 0
        for number in numbers:
            is_total = number
            get_sum = number % 10  # Вычисляем сумму цифр
            while number > 0:
                number //= 10
                get_sum += number % 10
            if get_sum % 7 == 0:
                total += is_total
        return total

    return f'результат: {get_sum()}'


print('V 1.0', func(), end='\n\n')


# V2.0 используем генератор вместо списка
@get_mem_time
def func():
    numbers = (number ** 3 for number in range(1, 1000000, 2))

    def get_sum():
        total = 0
        for number in numbers:
            is_total = number
            get_sum = number % 10  # Вычисляем сумму цифр
            while number > 0:
                number //= 10
                get_sum += number % 10
            if get_sum % 7 == 0:
                total += is_total
        return total

    return f'результат: {get_sum()}'


print('V 2.0', func(), end='\n\n')


# получили экономию памяти

# V2.1
@get_mem_time
def func():
    return f'результат: {sum(i for i in (number ** 3 for number in range(1, 1000000, 2)) if sum(map(lambda x: int(x), str(i))) % 7 == 0)}'


print('V 2.1', func(), end='\n\n')
'''Используя встроенные методы получил лаконичное решение в одну строчку, первому решению оно проигрывает по времени, а второму и по времени и по памяти, к сожалению. Можно ли это считать оптимизацией?'''
######################################################################################################################
print('######################################################################################################################')
'''Реализуйте структуру "доска задач".
Структура должна предусматривать наличие несольких очередей задач, например,
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения'''


class Turn:
    def __init__(self):
        self.tasks = []
        self.debagging = []
        self.compleated = []

    def add_task(self, task):
        self.tasks.append(task)

    def compleate(self):
        self.compleated.append(self.tasks.pop(0))

    def debagg(self):
        self.debagging.append(self.tasks.pop(0))

    def show(self):
        print(f'tasks: {self.tasks}', f'debagging: {self.debagging}', f'compleated: {self.compleated}', sep='\n')

    def debaging_compleate(self):
        self.compleated.append(self.debagging.pop(0))


# будем создавать список объектов класса Turn:

@get_mem_time
def turn_list(cls):
    list = []
    for i in range(100000):
        obj = cls
        obj.add_task('task1')
        list.append(obj)
    print(f'Количество объектов класса {cls}', len(list))
    return list[-1]


print(turn_list(Turn()), end='\n\n')


# создадим дочерний класс с атрибутами, хранящимися в списке
class Turn_2(Turn):
    __slots__ = ['tasks', 'debagging', 'compleated']


print(turn_list(Turn_2()), end='\n\n')  # получаем существенную экономию памяти


# создадим дочерний класс от дочернего класса, переопределим некоторые методы, вместо list используем deque
class Turn_3(Turn_2):
    def __init__(self):
        self.tasks = collections.deque()
        self.debagging = collections.deque()
        self.compleated = collections.deque()

    def compleate(self):
        self.compleated.append(self.tasks.popleft())

    def debagg(self):
        self.debagging.append(self.tasks.popleft())

    def debaging_compleate(self):
        self.compleated.append(self.debagging.popleft())


# создадим объекты классов
obj_T2 = Turn_2()
obj_T3 = Turn_3()

# будем добавлять задачи и потом их удалять как завершенные
@get_mem_time
def add_compleate(obj, n):
    for i in range(n):
        obj.add_task(i)

    for i in range(n):
        obj.compleate()



add_compleate(obj_T2, 100000)
add_compleate(obj_T3, 100000)
# Благодоря deque при работе с началом списка наблюдается прирост скорости

######################################################################################################################
print('######################################################################################################################')

"""Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ..."""


@get_mem_time
def f(n):
    def some_sum(n):
        return 1 if n == 1 else 1 + some_sum(n-1)/-2
    return some_sum(n)
print(f(100), end='\n\n')

@get_mem_time
def some_sum_2(n): # используем цикл вместо рекурсии
    el = 1
    s = 0
    for i in range(n):
        s += el
        el /= -2
    return s

print(some_sum_2(100))
# потребление памяти уменьшилось

