def simpleornot(n):
    if type(n) == int:
        if 0 < n < 1001:
            if n == 1 and n == 2:
                print(f'{n} - простое число')
            elif 0 not in [n % i for i in range(2, n)]:
                print(f'{n} - простое число')
            else:
                print(f'{n} - непростое число')
        else:
            print(f'Введите натурально число от 1 до 1000')
    else:
        print(f'Введите натурально число от 1 до 1000')


def find_deviders(n):
    if type(n) == int:
        if 0 < n < 1001:
            return [i for i in range(1, n + 1) if n % i == 0]
        else:
            print(f'Введите натурально число от 1 до 1000')
    else:
        print(f'Введите натурально число от 1 до 1000')


def showbigger(n):
    return max(find_deviders(n))

if __name__ == '__main__':
    simpleornot(900)
    print(find_deviders(121))
    print(showbigger(121))