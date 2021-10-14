def simpleornot(n, out=0):
    """
    Функция определяет простое или нет число
    :param n: натурально число от 1 до 1000
    :param out: 1 - выводим 1 или 0,
                0 - печатает
    :return: 1 для простого, 0 для непростого
    """
    if type(n) == int:
        if 0 < n < 1001:
            if n == 1 and n == 2:
                if out:
                    return 1
                else:
                    print(f'{n} - простое число')
            elif 0 not in [n % i for i in range(2, n)]:
                if out:
                    return 1
                else:
                    print(f'{n} - простое число')
            else:
                if out:
                    return 0
                else:
                    print(f'{n} - непростое число')
        else:
            print(f'Введите натурально число от 1 до 1000')
    else:
        print(f'Введите натурально число от 1 до 1000')


def find_deviders(n,out='all'):
    """
    Функция выводит список всех делителей
    :param n: натурально число от 1 до 1000
    :param out: 'all' - выводит все простые,
           'min' - выводит минимальный,
           'max' - выводит максимальный,
    :return: список всех делителей,
             или мин или макс из них
    """
    if type(n) == int:
        if 0 < n < 1001:
            all_div =[i for i in range(1, n + 1) if n % i == 0]
            if out == 'all': return all_div
            if out == 'max': return max(all_div)
            if out == 'min': return min(all_div)
        else:
            print(f'Введите натурально число от 1 до 1000')
    else:
        print(f'Введите натурально число от 1 до 1000')


def show_simpledeviders(n, out='all'):
    """
    Функция выводит список всех простых делителей,
    или минимальный или максимальный простой делитель
    :param n: натурально число от 1 до 1000
    :param out: 'all' - выводит все простые,
                'min' - выводит минимальный,
                'max' - выводит максимальный,
    :return: список, мин или макс  простых делителей.
    """
    deviders = find_deviders(n, 'all')
    simp_dev = [el for el in deviders if simpleornot(el,1)]
    if out == 'all': return simp_dev
    elif out == 'max': return max(simp_dev)
    elif out == 'min': return min(simp_dev)


def simple_multipliers(n):
    """
    Функция раскладывает число на простые множители
    :param n: натурально число от 1 до 1000
    :return: список всех делителей
    """
    ans = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            ans.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        ans.append(n)
    return ans



if __name__ == '__main__':
    n = 169
    simpleornot(n, 0)
    print(find_deviders(n))
    print(show_simpledeviders(n, 'max'))
    print(simple_multipliers(n))

