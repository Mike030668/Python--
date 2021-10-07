# -*- coding: utf-8 -*-
"""Lesson_4_Pro
В файле с логами   https://drive.google.com/open?id=1pKGu-u2Vvtx4xK8i2ZhOzE5rBXyO4qd8
 найти дату самого позднего лога (по метке времени)
"""

# для загрузки данных по ссылке
import gdown

# загружаем архив
file_path = 'https://drive.google.com/file/d/1pKGu-u2Vvtx4xK8i2ZhOzE5rBXyO4qd8/view'
file_id = str(file_path.split('/')[5:-1][0])
name_file = '../Lesson 3/text.txt'
gdown.download('https://drive.google.com/uc?id=' + file_id, name_file, quiet=False)

# Считать/скопировать текст из файла
f = open(name_file).readlines()
print(f)

text = []
for line in f:
  # этим split("\n")[0] берем берем 1ю часть, убирая "\n"
  print(line.split("\n")[0])
  text.append(line.split("\n")[0])

text[0]

dates = []
for elem in text:
  print(elem.split(",")[0]) 
  dates.append(elem.split(",")[0])

dates = [[data.split(' ')[0], data.split(' ')[1]] for data in dates]
dates

sort_dates = sorted(dates, key = lambda x: x[0],reverse = True)
sort_dates

print('Последний лог',sort_dates[0][0], 'числа в ', sort_dates[0][1])