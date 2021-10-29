import sys
import time

# декоратор
def get_memory(f):
    def checker(*args, **kwargs):
        start = time.time()
        data = f(*args, **kwargs)
        print(f'Memory:  {sys.getsizeof(data)}')
        return data
    return checker


@get_memory
def get_range_1(num):
    return [i for i in range(1, num)]

@get_memory
def get_range_2(num):
    data = []
    for i in range(1, num):
        data.append(i)
    return data

@get_memory
def get_range_3(num):
    return (i for i in range(1, num))


@get_memory
def get_range_4(num):
    for i in range(1, num):
        yield i

a = get_range_1(1000000)
print()
a = get_range_2(1000000)
print()
a = get_range_3(1000000)
print()
a = get_range_4(1000000)

