import divisor_master as dm
import random

# функция тестирования
def test_function(fun, test_lst):
    good_test = 0
    bad_test = 0
    bad_values = []

    for value in test_lst:
        try:
            fun(value)
            good_test += 1
        except Exception as e:
            print(e)
            bad_values.append(value)
            bad_test += 1

    if not len(bad_values):
        print('Все прошло хорошо!')
    else:
        print(f'удачных тестов {100 * good_test / len(test_lst)} %')
        print(f'плохих тестов {100 * bad_test / len(test_lst)} %')
    return bad_values


# тестовые наборы
test_lst_1 = [random.randint(1, 100) for i in range(100)]
test_lst_2 = [random.randrange(1, 100, 3)*(-1)**i for i in range(100)]
test_lst_3 = [random.random()*100 for i in range(100)]

p = [1, 0.1, 'r', 5, 10, 23.6, '34']
test_lst_4 = [random.choice(p) for i in range(100)]

# набор тестов
big_test = [test_lst_1, test_lst_2, test_lst_3, test_lst_4]

# смешанный тест
mix_test = []
for test in big_test:
    mix_test.extend(test)

# смешанный тест случайных 20
mix_test = random.sample(mix_test, 20)

print(f'Тест на наборе {mix_test}')

# список тестируемых функций
funlst = [dm.find_deviders,
          dm.simple_multipliers,
          dm.show_simpledeviders,
          dm.find_deviders]

# проход случайным тестом по функциям
for fun in funlst:
    print(f'функция {fun.__name__}')
    check = test_function(fun, mix_test)
    print(f'Значения дающие ошибку {check}')
    print()

