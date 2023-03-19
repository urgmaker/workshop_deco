# Задача 3
args_tuple = (1, 2, 3, 4)
d_args = {
    'arg_1': 1,
    'arg_2': 2,
    'arg_3': 3,
    'arg_4': 4
}


def func_3(arg_1, arg_2, arg_3, arg_4, *args, **kwargs):
    summand_1 = arg_1 + arg_2 + arg_3 + arg_4
    summand_2 = args_tuple[0] + args_tuple[1]
    summand_3 = d_args['arg_1']
    return summand_1 + summand_2 + summand_3


a = func_3(1, 2, 3, 4)
print(a)

# У меня сложилось ощущение, что я асболютно не понял формулировку задания Hard...
# Надеюсь, что я сделал то, что требовалось
