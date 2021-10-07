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
    return [i for i in range(10**6)]  # Сложность O(n)


@measure
def create_dict():
    # return {i: chr(i) for i in range(127)}  # Сложность линейная
    return {i: i for i in range(10**6)}  # Сложность O(n)


@measure
def create_dict_2():
    # return {i: chr(j) for i in range(127) for j in range(i + 1)}
    return {i: j for i in range(10**6) for j in
            range(i + 1)}  # Сложность O(n**2) т.к. значение высчитывается вторым циклом => выполняется медленнее


@measure
def add_obj(obj, val, index=None):
    if type(obj) == list:
        if index != None:
            obj.insert(index, val)  # Добавление в определённое место списка O(n)
            return obj
        else:
            return obj.append(val)  # Добавление в конец списка O(1)
    elif type(obj) == dict:
        obj[index] = val  # Добавление в словарь O(1)
        return obj


@measure
def get_elem(obj, key):  # Взятие элемента по индексу(ключу) O(1) для списка и словаря
    return obj[key]


@measure
def delete_elem(obj, key=None):
    if type(obj) == list:
        return obj.pop(key)  # Удаление элемента по индексу из списка O(n), если последний элемент O(1)
    elif type(obj) == dict:
        return obj.pop(key)  # Удаление из словаря O(1)


print('создание списка: ', end=" ")
my_list = create_list()

print('Добавление злемента в конец списка: ', end=" ")
add_obj(my_list, 30)
print(my_list[-10:])

print('Добавление злемента в начало списка: ', end=" ")
add_obj(my_list, 25, index=0)
print(my_list[:10])

print('Извлечение злемента списка: ', end=" ")
print(get_elem(my_list, 55))

print('Удаление злемента из начала списка: ', end=" ")
print(delete_elem(my_list, 0))

print('создание словаря: ', end=" ")
my_dict = create_dict()

# print('создание словаря 2й функцией: ', end=" ")  # долго выполняется
# my_dict = create_dict_2()

print('Добавляем элемент в словарь: ', end=" ")
add_obj(my_dict, 'A', index='a')

print('Извлекаем элемент из словаря: ', end=" ")
print(get_elem(my_dict, 'a'))

print('Удаление злемента словаря: ', end=" ")
print(delete_elem(my_dict, 'a'))

'''С временем выполнения не очень понятно. все операции показывают 0'''