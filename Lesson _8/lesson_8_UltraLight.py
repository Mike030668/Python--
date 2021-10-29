import random
import numpy as np

# Тернарный оператор
c = random.randint(1, 100)
b = random.randint(c, c ** 2)

a = b // c if b % c == 0 else b % c
print(c)
print(b)
print(a)
print()

# Генераторы последовательностей
a = [np.sin(x/2*np.pi) + np.cos(x/2*np.pi) for x in range(100)]
print(a)
print()

# декоратор
def split_sings(f):
    def checker(*args, **kwargs):
        data = f(*args, **kwargs)
        plus = list(filter(lambda x: x > 0, data))
        minus = list(filter(lambda x: x < 0, data))
        return (plus, minus)
    return checker

@split_sings
def get_randdata(num):
    data = np.random.standard_normal(num) * np.random.gumbel(num)
    return data

data = get_randdata(20)

print(data)
