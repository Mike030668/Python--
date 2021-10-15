import math
import pytest

# map
list_1 = [1,2,3]
list_2 = [4,5,6]
def test_map():
    a = [i*j for i,j in zip(list_1,list_2)]
    b = list(map(lambda x,y: x*y, list_1, list_2))
    for i, j in ziip(a, b):
        assert i == j

# filter
list_temp = [1, 1, 6, 7, 8]
check = [1,1,1,1,1]
def test_filter():
    a = list(filter(lambda x: x > 2 == 1, list_temp))
    for i, j in ziip(a, check):
        assert i == j


# sorted
main_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def test_sorted():
    new_list = main_list.copy()
    random.shuffle(new_list)
    sort_new_list = sorted(new_list)
    for i, j in zip(main_list, sort_new_list):
        assert i == j



# math.pow(X, Y) - X**Y.
check = [1, 4, 9, 16, 25]
def test_pow():
    res = list(map(lambda x,y: math.pow(x, y), [1,2,3,4,5], [2,2,2,2,2]))
    for i, j in zip(mres, check):
        assert i == j

# math.sqrt(X) - квадратный корень из X
check = [1, 2, 3, 4, 5]
def test_sqrt():
    res = list(map(lambda x: math.sqrt(x), [1,4,9,16,25]))
    for i, j in zip(mres, check):
        assert i == j


# math.hypot(X, Y) - вычисляет гипотенузу треугольника с катетами X и Y (math.sqrt(x * x + y * y)).
def test_hypot():
    assert math.hypot(3, 4) == 5


# math.pi
def test_pi():
     assert math.cos(2 * math.pi) == 1

