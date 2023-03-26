CNT = 0

def func_1(num_1, num_2):
    global CNT
    print('Значение счетчика после запуска функции func_1', CNT)
    CNT += 1
    return num_1 + num_2



def func_2(num_1, num_2):
    global CNT
    print('Значение счетчика после запуска функции func_2', CNT)
    CNT += 1
    return num_1 + num_2



func_1(1, 2)
func_2(5, 6)
print(f'Наши функции запустились {CNT} раза')



