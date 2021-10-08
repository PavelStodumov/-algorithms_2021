"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш.

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей.

Самый просто вариант хранения хешей - просто в оперативной памяти (в переменных).

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Обязательно усложните задачу! Добавьте сохранение хеша в файле и получение его из файла.
А если вы знаете как через Python работать с БД, привяжите к заданию БД и сохраняйте хеши там.
"""
import hashlib
import sqlite3

try:
    connection = sqlite3.connect('pass_db')
    cursor = connection.cursor()
    # cursor.execute('''DROP TABLE IF EXISTS passwords''')
    cursor.execute('CREATE TABLE IF NOT EXISTS passwords ('
                   'password TEXT);')
    insert_password = '''INSERT INTO passwords (password) VALUES (?);'''

    salt = input('Введите логин: ')

    password = hashlib.sha256(salt.encode() + input('Введите пароль: ').encode()).hexdigest()
    cursor.execute('''SELECT password FROM passwords''')
    if (password,) not in cursor.fetchall():
        cursor.execute(insert_password, (password,))

    cursor.execute('''SELECT password FROM passwords''')
    print(cursor.fetchall())  # список паролей, хранящихся в БД

    connection.commit()

    password = input(f'Введите пароль ещё раз для логина {salt}: ')
    cursor.execute('''SELECT password FROM passwords''')
    if (hashlib.sha256(salt.encode() + password.encode()).hexdigest(),) in cursor.fetchall():
        print('Вы ввели правильный пароль')
    else:
        print('Вы ввели неправильный пароль')

    cursor.close()
except Exception as ex:
    print(ex)

finally:
    connection.close()

'''Попробовал с БД. Пришлось соль сделать ввиде логина через ввод, иначе БД накапливала пароли, и в случае если первый раз вводишь новый пароль, а повторно какой-нибудь из тех, что уже есть в базе, ответ получается утвердительный, хотя пароли вводишь разные'''

# salt = 'salt'
# password = input('Введите пароль: ')
# pas = hashlib.sha256(salt.encode() + password.encode()).hexdigest()
#     print(pas, type(pas))
# password_t = input('Введите пароль ещё раз для проверки: ')
# if hashlib.sha256(salt.encode() + password_t.encode()).hexdigest() == pas:
#     print('Вы ввели правильный пароль')
# else:
#     print('Вы ввели неправильный пароль')
