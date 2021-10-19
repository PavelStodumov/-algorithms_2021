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
    def wrapper():
        m_start = memory_profiler.memory_usage()[0]
        t_start = default_timer()
        r = func()
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


# print('V 1.0', func(), end='\n\n')


# V2.0 используем list comprehensions вместо списка
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


# print('V 2.0', func(), end='\n\n')
# получили экономию памяти

# V2.1
@get_mem_time
def func():
    return f'результат: {sum(i for i in (number ** 3 for number in range(1, 1000000, 2)) if sum(map(lambda x: int(x), str(i))) % 7 == 0)}'


# print('V 2.1', func(), end='\n\n')
'''Используя встроенные методы получил лаконичное решение в одну строчку, первому решению оно проигрывает по времени, а второму и по времени и по памяти, к сожалению. Можно ли это считать оптимизацией?'''

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
def turn_list():
    list = []
    for i in range(100000):
        obj = Turn()

        obj.add_task('task1')
        list.append(obj)
    print(len(list))
    return list[-1]

print(turn_list())
