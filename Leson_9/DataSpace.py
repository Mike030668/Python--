import numpy as np
from scipy.spatial.distance import cosine


class DataSpace:
    """
    Измерение внутреннего пространства данных
    data: данные
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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    control_data = np.random.random(size=(10, 7))
    own_data = DataSpace(control_data)
    print()
    print(own_data)
    print()
    print(own_data.owncosin_space())
