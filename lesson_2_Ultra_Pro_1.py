import random
attempt = 0
chances = 10

print('Начнем игру угадай число?')
play = input('если да, то поставь + или - :')

if play == '+':
    print('Ура!! Ты в игре')
    print('У тебя ' + str(chances) + ' попыток')
    print('я загадал число от 0 до 100')
    number = random.randint(0, 100)

    while attempt < 10:
        figure = int(input('Напиши свое число '))
        attempt += 1
        if figure < number: print('Загадано больше твоего числа ')
        if figure > number: print('Загадано меньше твоего числа ')
        if figure == number: break
    if figure == number: print('Отлично! Число угадано с ' + str(attempt) + ' раз')
    if figure != number: print('Упс, пролет, было загадано число' + str(attempt))

else: print('Жаль, что ты сегодня не в духе ((')