def add_everything_up(a, b):
    try:
        sum_ = a + b
        return sum_
    except:
        sum_ = f'{a}{b}'
        return sum_


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
