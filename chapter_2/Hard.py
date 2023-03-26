CNT = 0
def outer_func(*args, **kwargs):
    # Теперь CNT принадлежил локальной области видимости функции outer_func
    # Это значит, что увеличение счетчика пойдет начиная со значения 4
    CNT = 4
    print("Это функция, которая объявляет внутри себя другую функцию")
    CNT += 1

    def func_sum_1(num_1, num_2):
        print(f'Это функция со значением счетчика {CNT}, которая была объявлена внутри другой функции')
        return num_1 + num_2

    return func_sum_1


result = outer_func()
print(result)
