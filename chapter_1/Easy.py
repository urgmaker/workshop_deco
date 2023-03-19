word = 'test'
count = 3


def func(*args, **kwargs):
    result_string = word * count
    result = ''.join(x.upper() if 4 <= i <= 7 else x.lower() for i, x in enumerate(result_string))
    return result


a = func(word, count)
print(a)

x = func
# Здесь я вижу, что в переменную "х" передана ссылка на функцию func,
# которая занимает место в пямяти по адресу 0x000002454A17F1F0
print(x)

# Исключение (возможно, я неправильно понял смысл 3 пункта?)
sum(x)