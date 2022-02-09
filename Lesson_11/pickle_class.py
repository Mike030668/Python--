import pickle
import numpy as np
from Data_cosdistance import Dist_cos

control_data = np.random.random(size=(3, 3))
own_data = Dist_cos(control_data)

f = open('own_data.pkl', 'wb')
pickle.dump(own_data, f)
f.close()

# Десериализация
f = open('own_data.pkl', 'rb')

own_data_new = pickle.load(f)

print(own_data)
print(own_data_new)

f.close()