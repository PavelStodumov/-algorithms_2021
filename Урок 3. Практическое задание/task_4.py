"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если есть, получаем
если нет, то вносить ее в кэш

url : хеш-url


Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации.

Задание творческое. Здесь нет жестких требований к выполнению.
"""
import hashlib

my_cache = {}
def caching(url, cache=my_cache):
    salt = 'salt'
    if url in cache:
        return cache[url]
    cache[url] = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
    return cache[url]


caching('vk')
print(my_cache)
caching('auto')
print(my_cache)
print(caching('vk'))