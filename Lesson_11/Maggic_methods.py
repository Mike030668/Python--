import numpy as np
from Data_cosdistance import Dist_cos

# https://habr.com/ru/post/186608/


control_data = np.random.random(size=(3, 3))
checked_data_1 = np.random.uniform(1, 3, size=(3, 3))
checked_data_2 = np.random.beta(2, 7, size=(3, 3))

own_data = Dist_cos(control_data)
data_1 = Dist_cos(checked_data_1)
data_2 = Dist_cos(checked_data_2)

print('Смотрим данные в созданных объектах класса')
print(own_data.data)
print(data_1.data)
print(data_2.data)
print()

print('Используем print для вывода описания объекта класса')
print(own_data)
print(data_1)
print(data_2)
print()

print(f'Свое пространство {own_data.ownspace()}')
print()

print('Получаем мин и макс расстояние своего объекта с другим объектом класса')
print(own_data.distance2classes(data_1))
print(own_data.distance2classes(data_2))
print()

print('Используем len(own_data) для проходу по объекту класса')
for i in range(len(own_data)):
    print(own_data[i])
print()

print('Итерируем по данным объекта класса')
for item in own_data:
    print(item)
print()

print('Складываем объекты класса')
new_data = data_1 + data_2
print(new_data)

print('Получаем мин и макс расстояние своего объекта с другим объектом класса')
print(own_data.distance2classes(new_data))
print()
print(f'Проверка равенства объектов класса {own_data == new_data}')
print(f'Проверка неравенства объектов класса {data_1 != data_2}')
print(f'Сравнение объектов класса {np.ones((3, 3)) * 5 > data_2}')
print(f'Проверка равенства объектов класса {np.zeros((3, 3)) < data_2}')

del (own_data, data_1, data_2, new_data)
print()

print('Создаем серию объектов класса на основе списка методом класса')
datas = (np.random.uniform(1, 3, size=(3, 3)) for _ in range(5))
cls_lst = Dist_cos.makeobject(datas)
for cls in cls_lst:
    print(cls)
