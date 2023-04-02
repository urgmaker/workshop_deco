from typing import Callable

CNT = 10

# Задача 1.1


def message_deco(some_func: Callable):
    print(f'Декорируем функцию {some_func}')

    def inner_func(*args, **kwargs):
        print('Покупайте наших котиков!')
        result = some_func(*args, **kwargs)
        return result

    return inner_func


@message_deco
def my_func(*args, **kwargs):
    print('Вызов my_func с произвольными параметрами')
    return f'Результат работы my_func с произвольными параметрами: {args}, {kwargs}'


my_func(5, 20)

# Задача 1.2