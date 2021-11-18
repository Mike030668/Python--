import DataSpace


class Distance_Spaces(DataSpace):
    """
    Измерение внутреннего пространства данных
    Вычисление расстояния между своими данными
    и внешними данными
    data: данные
    checked_data : внешние данные
    """
    # инициализации
    def __init__(self, data: object):
        DataSpace.__init__(self, data)

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
    control_data = np.random.random(size=(10, 7))
    checked_data = np.random.binomial(2, 0.7, size=(20, 7))
    own_data = Distance_Spaces(control_data)
    print()
    print(own_data)
    print()
    own_data.distance_spaces(checked_data)
#