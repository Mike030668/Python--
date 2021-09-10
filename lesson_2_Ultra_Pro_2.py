import random

attempt = 0
chances = 10
bord1 = 0
bord2 = 100

print('Начнем игру "Угадай твое число" ?')
play = input('если да, то поставь + или - :')

if play == '+':
    print('Загадай и запиши себе число от 0 до 100')
    print('И так, у меня ' + str(chances) + ' попыток')
    print('На каждый мой ответ:')
    print('- поставь   >   , если мое число больше твоего;')
    print('- поставь   <   , если мое число меньше твоего;')
    print('- поставь   =   , если я угадал;')
    print('ПОГНАЛИ')

    while attempt < chances:
        try:
            number = random.randint(bord1, bord2)
            # print(bord1-1, bord2+1)
        except:
            answer = '!'
            break
        print('Я говорю ' + str(number))
        check_answ = False
        while check_answ != True:
            answer = input('Ну как оно? - ')
            if answer in ('>', '<', '='):
                check_answ = True
            else:
                print('Ты ввел не тот знак, внимательнее!')

        attempt += 1
        if answer == '>':
            bord2 = number - 1
        elif answer == '<':
            bord1 = number + 1
        elif answer == '=':
            break

    if answer == '=': print('Отлично! Число угадано с ' + str(attempt) + ' раз')
    if answer == '!':
        print('Где-то ты ошибся!')
    else:
        real_answ = input('Упс, я пролет, а какое число было загадано ?')
        check_lst = range(bord1, bord2)
        # print(bord1-1, bord2+1)
        if int(real_answ) in check_lst:
            print('Все верно, ты выиграл')
        else:
            print('Где-то ты ошибся!')

else:
    print('Жаль, что ты сегодня не в духе ((')