"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: 
1) создайте простой список (list) и очередь (deque). Сделайте замеры и оцените что заполняется быстрее.
2) Выполните различные операции с каждым из объектов. Сделайте замеры и оцените, где и какие операции быстрее.

В первую очередь необходимо выполнить замеры для ф-ций appendleft, popleft, extendleft дека и для их аналогов у списков.
"""
import collections
from timeit import timeit

my_list = [i for i in range(10000)]
my_deq = collections.deque([i for i in range(10000)])

print('Время заполнения list: ', timeit('my_list', globals=globals()))
print('Время заполнения deque: ', timeit('my_deq', globals=globals()))

def ins_list(n, ls): # добавляем n элементов в начало списка
    for i in range(n):
        ls.insert(0, i)
    return ls

def ins_deq(n, deq):
    for i in range(n):
        deq.appendleft(i)
    return deq

def list_popleft(n, ls):
    for i in range(n):
        ls.pop(0)
    return ls

def deq_popleft(n, deq):
    for i in range(n):
        deq.popleft()
    return deq

def list_extendleft(n, ls):
    s = [i for i in range(n)]
    for i in s:
        ls.insert(0, i)
    return ls

def deq_extendleft(n, deq):
    s = [i for i in range(n)]
    deq.extendleft(s)
    return deq

def list_extend(n, ls):
    s = [i for i in range(n)]
    ls.extend(s)
    return ls

def deq_extend(n, deq):
    s = [i for i in range(n)]
    deq.extend(s)
    return deq

def get_elems_ls(n, ls):
    s = []
    for i in range(n):
        s.append(ls[i])
    return s

def get_elems_deq(n, deq):
    s = []
    for i in range(n):
        s.append(deq[i])
    return s

print('Добавим 100 элементов в начало list: ', timeit('ins_list(100, my_list)', globals=globals(), number=1000))
print('Добавим 100 элементов в начало deque: ', timeit('ins_deq(100, my_deq)', globals=globals(), number=1000))

print('Удалим 100 первых элементов list: ', timeit('list_popleft(100, my_list)', globals=globals(), number=1000))
print('Удалим 100 первых элементов deque: ', timeit('deq_popleft(100, my_deq)', globals=globals(), number=1000))

print('Добавим список из 100 элементов в начало list: ', timeit('list_extendleft(100, my_list)', globals=globals(), number=1000))
print('Добавим список из 100 элементов в начало deque: ', timeit('deq_extendleft(100, my_deq)', globals=globals(), number=1000))

print('Добавим список из 100 элементов list: ', timeit('list_extend(100, my_list)', globals=globals(), number=1000))
print('Добавим список из 100 элементов deque: ', timeit('deq_extend(100, my_deq)', globals=globals(), number=1000))

print('выберем 100 элементов по индексу list: ', timeit('get_elems_ls(100, my_list)', globals=globals(), number=10000))
print('выберем 100 элементов по индексу deque: ', timeit('get_elems_deq(100, my_deq)', globals=globals(), number=10000))


'''Создаются list и deque примерно за одинаковое время, а вот добавление элементов в начало происходит гораздо быстрее в deque. Добавление в конец происходит одинаково. По индексу элементы из списка беруться немного быстрее.'''