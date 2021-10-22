"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные по длине части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, Кучей...

Важно: стройте массив именно по формуле 2m+1
Потому что параметр m вам пригодится при поиске медианы, когда массив будет отсортирован.
Этот парамет m вам нужно запрашивать у пользователя.

[5, 3, 4, 3, 3, 3, 3]

[3, 3, 3, 3, 3, 4, 5]

my_lst
new_lts

arr[m]


from statistics import median

[3, 4, 3, 3, 5, 3, 3]

left = []
right = []

left == right and

for i in
    for
    left == right
    left.clear()
    right.clear()


"""
from random import randint
from timeit import timeit

# m = int(input())
m = 10
my_list = [randint(0, 100) for _ in range(2 * m + 1)]


def med1(ls):
    c = len(ls) // 2
    while True:
        left = []
        right = []
        for i in ls[:c]:
            if i < ls[c]:
                left.append(i)
            else:
                right.append(i)
        for i in ls[c + 1:]:
            if i < ls[c]:
                left.append(i)
            else:
                right.append(i)
        if len(left) == len(right):
            return f'медиана: {ls[c]}\n{ls}'
        ls = left + [ls[c]] + right


'''Идея такая: брать число из середины, остальной массив делить на два: в одном числа меньше взятого, в другом - меньше.
Если подмассивы разной длинны то складываем их и повторяем процедуру.'''


def med2(ls):
    c = len(ls) // 2
    i = 1
    while i < len(ls):
        if ls[i - 1] <= ls[i]:
            i += 1
        else:
            ls[i - 1], ls[i] = ls[i], ls[i - 1]
            if i > 1:
                i -= 1
    return f'медиана: {ls[c]}\n{ls}'
'''С гномьей сортировкой'''

print(med1(my_list))
print(f'Время выполнения моего цикла: {timeit("med1(my_list)", globals=globals(), number=10000)}')
print(med2(my_list))
print(f'Время выполнения гномьей сортировки: {timeit("med2(my_list)", globals=globals(), number=10000)}')