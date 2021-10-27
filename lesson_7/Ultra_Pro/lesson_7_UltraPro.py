# from google.colab import output
import json
import time
from datetime import datetime
'''
если не colab, то закомментировать запись выше
и в коде output.clear() в нескольких местах!
'''

# получение текущей даты и времени для отчета
def cur_time(x):
    return str(datetime.fromtimestamp(int(x)))


def privite_account():
    try:
        with open('report_account.txt') as f:
            balance = json.load(f)
        balance = int(balance)
    except:
        balance = 0
    main_menu = ('пополнить счет', 'совершить покупку', 'история покупок', 'выход')

    appeals = {1: 'Добрый день',
               2: 'для перехода в основное меню поставьте знак + : ',
               3: 'для выбора действия введите соответсвующую цифру: ',
               4: 'Введите сумму для пополнения счета: ',
               5: 'Введите сумму покупки: ',
               6: 'Введите название покупки: '
               }

    answers = {1: 'На вашем счете недостаточно средств, попoлните ваш счет!',
               2: 'Введено неверно, повторите!',
               3: 'Выход из меню, спасибо. До новых встреч!',
               4: 'Извините, пока нам больше нечего вам предложить, приходите в другой раз.'
               }
    try:
        with open('report_history.txt') as f:
            history = json.load(f)
    except:
        history = {}  # сбор истории

    account = balance
    addmoney = 0

    check_lst = [str(i + 1) for i in range(len(main_menu))]  # для получения индекса меню
    start = input(appeals[1] + ', ' + appeals[2])
    print()
    if start != '+':
        # output.clear()
        print(answers[4])
        print()
    else:
        # output.clear()
        work = True
        while work:
            check_form = False
            while not check_form:
                # output.clear()
                print('ОСНОВНОЕ МЕНЮ:')
                for i, el in enumerate(main_menu):
                    print(el + ' ' + str(i + 1))
                print('--------------------')
                print()
                # получаем ответ
                step_1 = input(appeals[3])
                # output.clear()
                print()
                if step_1 in check_lst:
                    check_form = True  # выход если верно
                else:
                    print(answers[2])
                    print()

            #######  сверка с отвепми #####
            if int(step_1) == 1:  # если пополнение счета
                check_form_1 = False
                while not check_form_1:
                    addmoney = input(appeals[4])
                    # output.clear()
                    print()
                    try:
                        if not float(addmoney):
                            print(answers[2])
                            print()
                        else:
                            check_form_1 = True  # выход если верно

                    except:
                        print(answers[2])
                        print()

                # output.clear()
                account += float(addmoney)
                curtime = cur_time(time.time())
                hist = {curtime + ' # Пополнение счета: ': float(addmoney)}
                history.update(hist)
                print('Пополнение счета', 'Ваш текущий остаток ' + str(account), sep='\n')
                print()

            if int(step_1) == 2:  # если покупка
                check_form_2 = False
                while not check_form_2:
                    reducemoney = input(appeals[5])
                    # output.clear()
                    try:
                        reducemoney = float(reducemoney)
                        if reducemoney <= account:
                            # check_form = True # выход если верно
                            buy = input(appeals[6])
                            # output.clear()
                            curtime = cur_time(time.time())
                            account -= reducemoney
                            hist = {curtime + ' # ' + buy: reducemoney}
                            # hist = {buy: reducemoney}
                            history.update(hist)
                            # print(history)
                            check_form_2 = True  # выход если верно
                            # output.clear()

                        else:
                            print(answers[1])  # недостаточно средств
                            print()
                            check_form_2 = True

                    except:
                        print(answers[2])
                        print()

            if int(step_1) == 3:  # если история
                # output.clear()
                print('ИСТОРИЯ ДЕЙСТВИЙ:')
                print('Входящий остаток ' + str(balance), sep='\n')
                for key, value in history.items():

                    if key.split('# ')[1] == 'Пополнение счета: ':
                        print(key, value)
                    else:
                        print(key.split('# ')[0] + 'Покупка: ' + key.split('# ')[1], value)
                print('--------------------')
                print('Ваш текущий остаток ' + str(account), sep='\n')
                print()
                # output.clear()

            if int(step_1) == 4:  # если выход
                with open('report_account.txt', 'w') as f:
                    json.dump(account, f)
                with open('report_history.txt', 'w') as f:
                    json.dump(history, f)
                print(answers[3])
                work = False


privite_account()
