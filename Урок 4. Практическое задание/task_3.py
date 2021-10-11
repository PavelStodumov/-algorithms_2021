"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Обязательно предложите еще свой вариант решения и также запрофилируйте!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!

Без аналитики задание считается не принятым
"""
from timeit import timeit
from cProfile import run


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num

def revers_4(enter_num):
    return ''.join(reversed(str(enter_num)))


num = 123456789

print('#' * 30 + 'revers_1(num)' + '#' * 30)
run('revers_1(num)')
print(timeit('revers_1(num)', globals=globals()))

print('#' * 30 + 'revers_2(num)' + '#' * 30)
run('revers_2(num)')
print(timeit('revers_2(num)', globals=globals()))

print('#' * 30 + 'revers_3(num)' + '#' * 30)
run('revers_3(num)')
print(timeit('revers_3(num)', globals=globals()))

print('#' * 30 + 'revers_4(num)' + '#' * 30)
run('revers_4(num)')
print(timeit('revers_4(num)', globals=globals()))

'''revers_1 реализована через рекурсию. Самое неэффективное решение. для 9-значного числа вызывается 13 функций
revers_2 цикл выполняет ряд математическихопераций на каждой итерации. 
revers_3 срез строки, самое быстрое решение с использованием встроенных методов работы со строками.
revers_4 реализовано с помощью встроенной функции, быстрее чем цикл, но медленнее среза.
'''