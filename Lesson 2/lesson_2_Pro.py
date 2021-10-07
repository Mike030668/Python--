# 6. Найти сумму цифр числа.
# 7. Найти сумму цифр числа.
fig = input('введите число')
summma = 0
prod = 1
for el in fig:
    summma += int(el)
    prod *= int(el)
print('сумма цифр числа ' + fig + ' = ' + str(summma))
print('произведение цифр числа ' + fig + ' = ' + str(prod))

# 8. Дать ответ на вопрос: есть ли среди цифр числа 5?
fig = input('введите число')
check_fig = '5'
i = 0
for el in fig:
    if el == check_fig:
        print("Есть число " + check_fig + ' в ' + fig)
        break
    else:
        if i == len(fig) - 1:
            print("Нет числа " + check_fig + ' в ' + fig)
    i += 1

# 9. Найти максимальную цифру в числе
fig = input('введите число')
max_num = 0
for el in fig:
    if int(el) > max_num:
        max_num = int(el)
print('В числе ' + fig + ' макс.число ', max_num)

# 10. Найти количество цифр 5 в числе
fig = input('введите число')
check_fig = '5'
qty = 0
for el in fig:
    if el == check_fig:
        qty += 1
print('В числе ' + fig + ' ' + check_fig + ' - ' + str(qty) + ' раз')
