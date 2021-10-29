import random
import numpy as np

# Тернарный оператор
c = random.randint(1, 100)
b = random.randint(c, c ** 2)

a = b // c if b % c == 0 else b % c
print(c)
print(b)
print(a)

# Генераторы последовательностей

a = [np.sin(x/2*np.pi) + np.cos(x/2*np.pi) for x in range(100)]
print(a)

# декоратор
def split_sings(f):
    def checker(*args, **kwargs):
        data = f(*args, **kwargs)
        plus = list(filter(lambda x: x > 0, data))
        # assert isinstance(data, object)
        minus = list(filter(lambda x: x < 0, data))
        return plus, minus
    return checker

@split_sings
def get_rand(num):
    data = np.random.standard_normal(num)*np.random.gumbel(num)
    return data

plus, minus = get_rand(20)

print(plus)
print(minus)