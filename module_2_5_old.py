# Создайте функцию def print_params, которая в своем теле будет распечатывать
# переданное значение из параметра 2 раза!
# Вызовите данную функцию несколько раз в том же файле

import random


def print_param():
    day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    today = random.choice(day)
    return today


today = 'Today is ' + print_param()
print(today)
print(today)
print('-------------------------------')


# последовательный вывод дней недели функция плюс цикл for:
def print_params(day):
    day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    for i in day:
        print('Today is ' + i)
    print(' ')


print_params(day='i')
print_params(day='i')
