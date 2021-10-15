import random


def f(a, n, out: object = None):
    if type(a) == list:
        out = []
        for i in range(n):
            out.append(random.choice(a))
        return out
    else:
        'Ошибка! Принимается только список'
    return out


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    names = ['Маша',
             'Федя',
             'Жора',
             'Гоша',
             'Коля',
             'Паша',
             'Саша',
             'Инна',
             'Нюра',
             'Гога',
             'Боря',
             'Лика',
             'Лера',
             'Дуня',
             'Варя',
             'Люся',
             'Марго',
             'Даря',
             'Тима',
             'Вика',
             ]

    d = f(names, 100)
    print(d)
