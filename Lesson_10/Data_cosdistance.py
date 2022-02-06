import numpy as np
from scipy.spatial.distance import cosine


class Dist_cos():
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

    # Уничтожение созданных классов
    def __del__(self):
        class_name = self.__class__.__name__
        print('{} уничтожен'.format(class_name))

    # вывод
    def __str__(self):
        return f'Данные: ({self.data})'

    def owncosin_space(self):
        space = []
        for i in range(self.data.shape[0]):
            for j in range(i, self.data.shape[0]):
                cos = cosine(self.data[i], self.data[j])
                space.append(cos)
        return space

    def cosin_distance(self, checked_data):
        distance = []
        for i in range(self.data.shape[0]):
            for j in range(checked_data.shape[0]):
                cos = cosine(self.data[i], checked_data[j])
                distance.append(cos)
        return distance

    def distance_spaces(self, checked_data):
        own_space = self.owncosin_space()
        distance = self.cosin_distance(checked_data)
        own_max = max(own_space)
        own_min = min(own_space)
        distance_max = max(distance)
        distance_min = min(distance)
        if distance_min > own_min and distance_max < own_max:
            return print(f'Данные {(distance_min, distance_max)} из контрольной области {(own_min, own_max)}')
        else:
            return print(f'Данные {(distance_min, distance_max)} вне контрольной области {(own_min, own_max)}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    control_data = np.random.random(size=(1,1))
    # checked_data = np.random.binomial(2, 0.7, size=(20, 7))
    own_data = Dist_cos(control_data)
    #print()
    print(own_data)
    #print()
    #own_data.distance_spaces(checked_data)
