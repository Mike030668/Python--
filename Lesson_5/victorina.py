import random

def rand_dictionary(dic, k):
    """
  функция создает случайный словарь
  из исходного словаря
  :param dic: исходный словарь
  :param k: размер нового словаря
  :return: случайный словарь из dic размера k
           или размера исходного при k более
           размера исходного
  """
    # формируем случайные индексы случайного словаря
    if k < len(dic):
        rand_idx = random.sample(range(len(dic)), k)
    else:
        rand_idx = random.sample(range(len(fam_bthd)), len(fam_bthd))

    # получаем ключи и значения исходного словаря
    keys = list(dic.keys())
    values = list(dic.values())

    # формируем случайные  ключи и значения к ним
    rand_values = [el for i, el in enumerate(values) if i in rand_idx]
    rand_keys = [el for i, el in enumerate(keys) if i in rand_idx]

    # выводим случайный словарь
    return dict(zip(rand_keys, rand_values))


def start_play(n=5):
    """
    функция запускает игру викторина
    :param n: количество вопросов, по умолчанию 5
    """
    step = input('Давай сыграем в Викторину, поставь + если готов' + ': ')
    print('---------------------------------------------')
    print()

    # словарь знаменитостей, можно наращивать
    fam_bthd = {'Константин Станиславский': '17.01.1863',
                'Майя Булгакова': '19.05.1932',
                'Сергей Бугаев': '28.03.1966',
                'Александр Кайдановский': '23.07.1946',
                'Михаил Евдокимов': '05.12.1957',
                'Джо Дассен': '05.11.1938',
                'Вивьен Ли': '05.11.1913',
                'Михаил Шемякин': '04.05.1943',
                'Александр Керенский': '22.04.1881',
                'Эрих Мария Ремарк': '22.06.1898'
                }

    # кортеж месяцев
    months = ('январь', 'февраль', 'март', 'апрель', 'май', 'июнь',
              'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь')

    # кортеж десятков
    des = ('двадцать', 'тридцать')
    # кортеж единиц
    edn = ('первое', 'второе', 'третье', 'четвертое', 'пятое',
           'шестое', 'седьмое', 'восьмое', 'девятое')
    dacad = ('десятое', 'двадцатое', 'тридцатое')
    # кортеж от 10 до 19
    specil = ('один', 'две', 'три', 'четыр', 'пять',
              'шесть', 'семь', 'восемь', 'девять', 'надцатое')

    if step == '+':
        print('ОК! Вводи дни рождения называемых мной знаменитостей в формате dd.mm.yyyy ')
        ready2play = True
        while ready2play:
            rand_fam_bthd = rand_dictionary(fam_bthd, n)  # формируем случайный словарь
            good_answ = 0  # счетчик верных ответов
            bad_answ = 0  # счетчик неверных ответов
            for chel in rand_fam_bthd.keys():  # fam_bthd.keys():
                # контроль корректности ввода
                check_form = False
                while not check_form:
                    # получаем ответ
                    step = input('День рождения ' + chel + ': ').split('.')
                    # сверка соответствия формату
                    if len(step) == 3 and \
                            (len(step[0]) == 2 and len(step[1]) == 2 and len(step[2]) == 4):
                        check_form = True  # выход если верно
                    else:
                        print('введено не в формате dd.mm.yyyy')

                check = 0  # счетчик совпадений
                bithday = rand_fam_bthd[chel].split('.')  # fam_bthd[chel].split('.')
                for i in range(len(step)):
                    if bithday[i] == step[i]: check += 1
                if check == 3:
                    good_answ += 1  # если счетчик 3, ответ верен и плюсуем
                else:
                    bad_answ += 1  # если счетчик не 3, ответ неверен и плюсуем
                    # получаем индекс месяца, убрав 0 если есть
                    idx = int(bithday[1].strip('0')) - 1

                    # получаем день
                    day = bithday[0]
                    # от 1 до 9
                    if day[0] == '0' or day == '10':
                        day = edn[int(day[1:]) - 1]
                    # от 11 до 19
                    elif day[0] == '1' and day[0] != '0':
                        day = specil[int(day[1:]) - 1] + specil[-1]
                    # 10,20,30
                    elif day in ('10', '20', '30'):
                        day_ = dacad[int(day[0]) - 1]
                    # другие
                    else:
                        day = des[int(day[0]) - 2] + ' ' + edn[int(day[1:]) - 1]
                    print('НЕВЕРНО, правильный ответ -', day, months[idx], bithday[2], sep=' ')

            print('---------------------------------------------')
            print()
            print('Верных ответов: ', good_answ)
            print('Неверных ответов: ', bad_answ)
            print('Процент точности: ', round(100 * good_answ / len(fam_bthd.keys()), 1), '%')
            print()
            step = input('Сыграем еще? Поставь + если готов' + ': ')
            print('---------------------------------------------')
            print()
            if step == '+':
                pass
            else:
                print('---------------------------------------------')
                print()
                print('Спасибо за игру, до новых встреч!')
                ready2play = False
    else:
        print('Жаль, что ты сегодня не в духе ((')


if __name__ == '__main__':
    start_play()
