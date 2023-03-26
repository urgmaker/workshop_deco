# Задача 1
CNT = 0


def func_sum(num_1, num_2):
    global CNT
    print('Значение счетчика после запуска функции func_1', CNT)
    CNT += 1
    return num_1 + num_2



def func_multiply(num_1, num_2):
    global CNT
    print('Значение счетчика после запуска функции func_2', CNT)
    CNT += 1
    return num_1 * num_2


def func_division(num_1, num_2):
    global CNT
    print('Значение счетчика после запуска функции func_3', CNT)
    CNT += 1
    return num_1 / num_2


func_sum(1, 2)
func_multiply(5, 6)
func_division(10, 5)
print(f'Наши функции запустились {CNT} раза')


# Задача 2
def outer_func(*args, **kwargs):
    print("Это функция, которая объявляет внутри себя другую функцию")

    def func_sum_1(num_1, num_2):
        print('Это функция, которая была объявлена внутри другой функции')
        return num_1 + num_2

    return func_sum_1

# Задача 3
# Здесь я наблюдаю, что при вызове внешней функции я получаю объек в локальной области видимости
result = outer_func()
print(result)

# Задача 4
# Вызываю функцию из полученной переменной
print(result(10, 20))