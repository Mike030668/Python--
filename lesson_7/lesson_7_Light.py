import csv

car_data = []
# Считывание файла построчно
f = open('data_text')
for line in f:
    line = line.lstrip(' ').split("\n")[0]
    line = line.split(' ')
    for _ in range(5):
        try: line.remove('')
        except: pass
    car_data.append(line)

f.close()
print(car_data)

with open('example.csv', 'w') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerows(car_data)
print('Writing complete!')