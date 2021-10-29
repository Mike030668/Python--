import time
import numpy as np
import sys

# декоратор
def split_sings(f):
    def checker(*args, **kwargs):
        start = time.time()
        data_t = f(*args, **kwargs)
        print(f'время до декоратора {data_t[1]}')
        plus = list(filter(lambda x: x > 0, data_t[0]))
        minus = list(filter(lambda x: x < 0, data_t[0]))
        return (plus, minus), time.time() - start

    return checker


@split_sings
def get_randdata(num):
    start = time.time()
    data = np.random.standard_normal(num) * np.random.gumbel(num)
    return data, time.time() - start


data, time_data = get_randdata(2000)

print(data[0])
print(data[1])
print(f'время после декоратора {time_data}')
print()


# декоратор
def get_time(f):
    def checker(*args, **kwargs):
        start = time.time()
        data = f(*args, **kwargs)
        print(f'время процесса {time.time() - start}')
        return data

    return checker


@get_time
def get_range_1(num):
    return [i for i in range(1, num)]

@get_time
def get_range_2(num):
    data = []
    for i in range(1, num):
        data.append(i)
    return data

@get_time
def get_range_3(num):
    return np.arange(1,num)

@get_time
def get_range_4(num):
    return list(map(lambda x: x , range(1,num)))

@get_time
def get_range_5(num):
    return list(filter(lambda x: x , range(1,num)))

@get_time
def get_range_6(num):
    for i in range(1, num):
        yield i

a = get_range_1(1000000)
print(len(a))
print()
a = get_range_2(1000000)
print(len(a))
print()
a = get_range_3(1000000)
print(len(a))
print()
a = get_range_4(1000000)
print(len(a))
print()
a = get_range_5(1000000)
print(len(a))
print()
a = get_range_6(1000000)
print(next(a))