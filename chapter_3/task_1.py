from typing import Callable
from datetime import datetime as dt
from time import sleep

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


def message_deco_with_param(info_message: str):
    def new_message_deco(some_func: Callable):
        def inner_func(*args, **kwargs):
            nonlocal info_message
            info_message = info_message.upper()
            print(info_message)
            return some_func(*args, **kwargs)
        return inner_func
    return new_message_deco


@message_deco_with_param(info_message='исследование параметризованного декоратора')
def my_func(*args, **kwargs):
    print('Вызов my_func с произвольными параметрами')
    return f'Результат работы my_func с произвольными параметрами: {args}, {kwargs}'


my_func(5, 20)


# Задача 2.1
#В этой задаче я сломал голову, так и не сделал ее. Подскажи, тут нужен блок try-except? Мне непонятно как реализовать исключение в самом декораторе
def exception_deco(some_func: Callable):
    def inner_function(*args, **kwargs):
        print('Пытаюсь выполнить деление')
        result = some_func(*args, **kwargs)
    return inner_function


@exception_deco
def division(a, b):
    try:
        return a / b
    except:
        print('Ошибка ввода данных')

division(10, 10)
division(1, '1')

# Задача 4.1

def time_it_deco(some_func: Callable) -> Callable:
    def inner(*args, **kwargs):
        start = dt.now()
        sleep(1)
        result = some_func(*args, **kwargs)
        # Выполняю задачу 4.2
        print(f'Функция {my_function} выполняется: {dt.now() - start}') # вероятно это не то, что требуется
        # у меня должно выйти на экран "my_function",
        # но вывод <function time_it_deco.<locals>.inner at 0x0000026F2C1D2040>
        return result
    return inner


@time_it_deco
def my_function(param_1, param_2):
    print(f'Вызов my_function с параметрами: {param_1}, {param_2}')
    return f'Результат работы my_function с параметрами: {param_1}, {param_2}'


my_function(10, 20)