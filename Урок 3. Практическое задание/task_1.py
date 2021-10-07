"""
Задание 1.

Реализуйте свои пользовательские функции, в которых реализуйте:

a) заполнение списка и словаря,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
   И укажите сложность каждой ф-ции, которую вы применяете для заполнения.
   У этих ф-ций может быть разная сложность. Поэтому время заполнения списка и словаря может как совпадать, так и отличаться.
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему
   И укажите сложность ф-ций, которые вы используете для операций.
   Операцию clear() не используем.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""
import time


def measure(func):

    def wrapper(*args, **kwargs):
        start = time.time()
        lst = func(*args, **kwargs)
        print(f'Время выполнения: {time.time() - start}')
        return lst


    return wrapper


@measure
def create_list():
    # return [chr(i) for i in range(127)]  # хотел выводить таблицу ascii но элементов мало для замера
    return [i for i in range(10000)]  # Сложность линейная

@measure
def create_dict():
    # return {i: chr(i) for i in range(127)}  # Сложность линейная
    return {i: i for i in range(10000)}  # Сложность линейная

@measure
def create_dict_2():
    # return {i: chr(j) for i in range(127) for j in range(i + 1)}
    return {i: chr(j) for i in range(10000) for j in
            range(i + 1)}  # Сложность квадратичная т.к. значение высчитывается вторым циклом => выполняется медленнее

@measure
def add_list(list, val, index=None):
    if index != None:
        list.insert(index, val)
        return list
    else:
        return list.append(val)









my_list = create_list()
add_list(my_list, 30)
print(my_list[-10:])
add_list(my_list,25, index=0)
print(my_list[:10])