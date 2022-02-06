import pytest
from Data_cosdistance import Dist_cos
# https://docs.pytest.org/en/latest/index.html

class Data_cosdistance_pytest:

    def setup(self):
        self.data = Dist_cos(np.random.random(size=(2, 2)))
        print('Start test!')