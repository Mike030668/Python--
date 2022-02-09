import numpy as np
from scipy.spatial.distance import cosine


class Dist_cos:
    """
    Измерение внутреннего пространства данных
    Вычисление расстояния между своими данными
    и внешними данными
    data: данные
    checked_data : внешние данные
    """

    # инициализации
    def __init__(self, data: object):
        self.data = data

    # вывод
    def __str__(self) -> str:
        return f'Собственное пространство класса: ({self.cosin_distance(self.data, self.data)})'

    # Уничтожение поданного значения
    def __del__(self):
        del self.data

    def __getitem__(self, key):
        if isinstance(key, int):
            return self.data[key]  # Если index является числом, вернуть напрямую
        if isinstance(key, slice):
            slicedkeys = list(self.data.keys())[key]  # Если index является типом слайса, вернуть словарь
            return {k: self.data[k] for k in slicedkeys}
        else:
            raise TypeError

    def __len__(self):
        return self.data.shape[0]

    def __add__(self, other):  # +
        other = self.__checktype__(other)
        return Dist_cos(self.data + other)

    def __eq__(self, other):  # ==
        other = self.__checktype__(other)
        own_min, own_max, distance_min, distance_max = self.estimate_datas(self.data, other)
        if distance_min > own_min and distance_max < own_max: return True
        else: return False

    def __lt__(self, other):  # <
        other = self.__checktype__(other)
        own_min, own_max, distance_min, distance_max = self.estimate_datas(self.data, other)
        if distance_max < own_min: return True
        else: return False

    def __le__(self, other):  # <=
        other = self.__checktype__(other)
        own_min, own_max, distance_min, distance_max = self.estimate_datas(self.data, other)
        if distance_max <= own_min: return True
        else: return False

    def __gt__(self, other):  # >
        other = self.__checktype__(other)
        own_min, own_max, distance_min, distance_max = self.estimate_datas(self.data, other)
        if distance_min > own_max: return True
        else: return False

    def __gt__(self, other):  # >=
        other = self.__checktype__(other)
        own_min, own_max, distance_min, distance_max = self.estimate_datas(self.data, other)
        if distance_min >= own_max: return True
        else: return False

    def __getstate__(self):
        return self.data

    def __setstate__(self, state):
        self.data = state

    def __checktype__(self, other):
        if type(other) == int or type(other) == float:
            raise TypeError('Должен быть или объект самого класса или нампи или список')
        elif isinstance(other, Dist_cos): return other.data
        elif isinstance(other, list) or isinstance(other, np): return other
        else: raise TypeError('Должен быть или объект самого класса или нампи или список')

    def distance2classes(self, other):
        """
        :param other: экземпляр того же класса или массив
        :return: возвращаем min(distance), max(distance)
        """
        if isinstance(other, Dist_cos):
            return self.estimate_datas(self.data, other.data)[2:]  # возвращаем min(distance), max(distance)
        else:
            return self.estimate_datas(self.data, other)[2:]  # возвращаем min(distance), max(distance)

    def cosin_distance(self, somedata_1, somedata_2):
        """
        :param somedata_1, somedata_2: массивы численных данных
        :return: возвращаем массив кос_расстояний между массивами
        """
        distance = []
        for i in range(somedata_1.shape[0]):
            for j in range(somedata_2.shape[0]):
                cos = cosine(somedata_1[i], somedata_2[j])
                distance.append(cos)
        return np.array(distance)

    def ownspace(self):
        """
        :return: возвращаем массив кос_расстояний внутри самого класса
        """
        return self.cosin_distance(self.data, self.data)

    def estimate_datas(self, own_data, other_data):
        """
        :param other: экземпляр того же класса или массив
        :return: возвращаем min(own_space), max(own_space), min(distance), max(distance)
        """
        own_space = self.cosin_distance(own_data, own_data)
        distance = self.cosin_distance(other_data, own_data)
        return min(own_space), max(own_space), min(distance), max(distance)

    def show_compare(self, own_data, other_data):
        """
        выводим сравнительную информацию в печатном виде
        """
        own_min, own_max, distance_min, distance_max = self.estimate_datas(own_data, other_data)
        if distance_min > own_min and distance_max < own_max:
            print(f'Данные {(distance_min, distance_max)} из контрольной области {(own_min, own_max)}')
        else:
            print(f'Данные {(distance_min, distance_max)} вне контрольной области {(own_min, own_max)}')

    @staticmethod
    def stat_method():

        pass

    @classmethod
    def makeobject(cls, list_data):
        """
        :param list_data: list данных для создаваемых объектов класса
        :return: возвращаем список объектов класса
        """
        list_cls = []
        for data in list_data:
            list_cls.append(cls(data))
        return list_cls


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
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
    print(f'Сравнение объектов класса {np.ones((3, 3))*5 > data_2}')
    print(f'Проверка равенства объектов класса {np.zeros((3,3)) < data_2}')

    del (own_data, data_1, data_2, new_data)
