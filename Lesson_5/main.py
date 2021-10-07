import divisor_master
n = 344
divisor_master.simpleornot(n, 0)
a = divisor_master.find_deviders(n)
print(f'все делители числа {n} это {a}')

a = divisor_master.show_simpledeviders(n, 'max')
print(f'самый большой простой делитель числа {n} это {a}')

a = divisor_master.simple_multipliers(n)
print(f'все простые множители числа {n} это {a}')

a = divisor_master.find_deviders(n, 'max')
print(f'самый большой делитель числа {n} это {a}')
