import DataSpace
from scipy.spatial.distance import euclidean


class Distance_Datas(DataSpace):
    """
    Измерение внутреннего пространства данных (выбор типа)
    Вычисление расстояния по типу между своими данными
    и внешними данными
    data: данные
    checked_data : внешние данные
    type: тип расстояния
    """

    # инициализации
    def __init__(self, data, dist_type) -> object:
        super().__init__(data)
        self.type_dist = dist_type

    def own_euclid_space(self):
        space = []
        for i in range(self.data.shape[0]):
            for j in range(i, self.data.shape[0]):
                euclid = euclidean(self.data[i], self.data[j])
                space.append(euclid)
        return space

    @property
    def distance(self):
        if self.type_dist == 'cos_dis':
            return self.owncosin_space(self, checked_data)
        elif self.type_dist == 'euclid_dis':
            return self.own_euclid_space(self, checked_data)
        else:
            print(f"Введите 'cos_dis' или 'euclid_dis'")

    def __cosin_distance(self, checked_data):
        distance = []
        for i in range(self.data.shape[0]):
            for j in range(checked_data.shape[0]):
                cos = cosine(self.data[i], checked_data[j])
                distance.append(cos)
        return distance

    def __euclid_distance(self, checked_data):
        distance = []
        for i in range(self.data.shape[0]):
            for j in range(checked_data.shape[0]):
                euclid = euclidean(self.data[i], checked_data[j])
                distance.append(euclid)
        return distance

    def distance_spaces(self, checked_data):
        if self.type_dist == 'cos_dis':
            own_space = self.owncosin_space()
            distance = self.__cosin_distance(checked_data)
        elif self.type_dist == 'euclid_dis':
            own_space = self.own_euclid_space()
            distance = self.__euclid_distance(checked_data)
        own_max = max(own_space)
        own_min = min(own_space)
        distance_max = max(distance)
        distance_min = min(distance)
        if distance_min > own_min and distance_max < own_max:
            return print(f'Данные {(distance_min, distance_max)} из контрольной области {(own_min, own_max)} на основе {self.type_dist}')
        else:
            return print(f'Данные {(distance_min, distance_max)} вне контрольной области {(own_min, own_max)} на основе {self.type_dist}')


control_data = np.random.random(size=(10, 7))
checked_data = np.random.binomial(2, 0.7, size=(20, 7))

own_data_cos = Distance_Datas(control_data, 'cos_dis')
print(own_data_cos)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    control_data = np.random.random(size=(10, 7))
    checked_data = np.random.binomial(2, 0.7, size=(20, 7))

    own_data_cos = Distance_Datas(control_data, 'cos_dis')
    print(own_data_cos)
    print()
    own_data_cos.distance_spaces(checked_data)
    print()
    own_data_euc = Distance_Datas(control_data, 'euclid_dis')
    print(own_data_euc)
    print()
    own_data_euc.distance_spaces(checked_data)
