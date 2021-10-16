"""
2. Написать программу сложения и умножения двух шестнадцатиричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)

__mul__
__add__

Пример:
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’]
Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

1. вариант
defaultdict(list)
int(, 16)
reduce

2. вариант
class HexNumber:
    __add__
    __mul__

hx = HexNumber
hx + hx
hex()
"""

import collections


def get_sum(*args):
    return list('%X' % sum(int(''.join(i), 16) for i in args))


def get_mul(*args):
    m = 1
    for i in args:
        m *= int(''.join(i), 16)
    return list('%X' % m)


num_1 = list(collections.deque(input()))
num_2 = list(collections.deque(input()))

print(num_1)
print(num_2)
print(get_sum(num_1, num_2))
print(get_mul(num_1, num_2))



class HexClass:
    def __init__(self, obj):
        self.hex = collections.deque(obj)
        self.obj = obj

    def __add__(self, other):
        return list('%X' % sum([int(self.obj, 16), int(other.obj, 16)]))
        # return HexClass(''.join(list('%X' % sum([int(self.obj, 16), int(other.obj, 16)]))))

    def __mul__(self, other):
        m = int(self.obj, 16) * int(other.obj, 16)
        return list('%X' % m)

    def __str__(self):
        return str(self.hex)


a = HexClass('A2')
b = HexClass('C4F')
print(a)
print(b)
print(a + b)
print(a * b)
