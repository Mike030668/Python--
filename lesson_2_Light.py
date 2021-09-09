# LIGHT
# 1. Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
for i in range(5):
    print(str(i + 1), 0)

# 2. пользователь в цикле вводит 10 цифр. Найти количество введенных пользователем цифр 5.
qty = 0
control_fig: int = 5
attempt = 10

for i in range(attempt):
    fig = int(input('введите цифру'))

    if fig == control_fig:
        qty += 1
    else:
        pass

print(f'число {str(control_fig)} введено {str(qty)} раз')

# 2. Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
result = 0
for i in range(1, 101):
    result += i
print('сумма от 1 до 100 = ', result)

# 3. Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
fractal: int = 1
i: int = 1
while i != 11:
    fractal *= i
    i += 1
print("произведение от 1 до 10 = ", fractal)

# 4. Вывести цифры числа на каждой строчке.
fig = input('введите число')
for el in fig:
    print(el)