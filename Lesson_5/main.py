import divisor_master as dm
import random

def test_function(fun, test_lst):
    good_test = 0
    bad_test = 0
    bad_values = []

    for value in test_lst:
        try:
            res = fun(value)
            bad_test += 1
        except:
            print('Я нашел не число!')
            bad_values.append(value)
            bad_test += 1

    if not len(bad_values):
        print('Все прошло хорошо!')
    else:
        print(f'удачных тестов {100 * good_test / len(test_lst)} %')
        print(f'плохих тестов {100 * bad_test / len(test_lst)} %')
    return bad_values



test_lst_1 = [random.randint(1, 1000) for i in range(100)]
test_lst_2 = [random.randrange(1, 1000, 3) for i in range(100)]
test_lst_3 = [random.random()*100 for i in range(100)]

p = [1, 0.1, 'r', 5, 10, 23.6, '34']
test_lst_4 = [random.choice(p) for i in range(100)]

big_test = [test_lst_1, test_lst_2, test_lst_3, test_lst_4]
one_test = random.choice(big_test)

print(f'Тест на наборе {one_test}')

funlst = [dm.find_deviders,
          dm.simple_multipliers,
          dm.show_simpledeviders,
          dm.find_deviders]

for fun in funlst:
    print(f'функция {fun}')
    check = test_function(fun, one_test)
    print(check)

