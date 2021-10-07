import gdown
# загружаем архив
file_path = 'https://drive.google.com/file/d/15fBsTB1ZU_BzEw5SJmlOMX2uuyi1xN1-/view?usp=sharing'
file_id = str(file_path.split('/')[5:-1][0])
name_file = '../text.txt'
gdown.download('https://drive.google.com/uc?id=' + file_id, name_file, quiet=False)


# Считать/скопировать текст из файла
f = open('../text.txt').readlines()
print(f)

text = ''
for line in f:
  # этим split("\n")[0] берем берем 1ю часть, убирая "\n"
  text += line.split("\n")[0]
print(text)


# методами строк очистить текст от знаков препинания;
element_lst = ',.-—;()!«»!?'
for element in element_lst:
    print(element)
    text = text.replace(element," ")
print(text)


# сформировать list со словами (split);
text = text.split()
print(text)


# привести все слова к нижнему регистру (map);
text = list(map(lambda x: x.lower(), text))
print(text)


# получить из list пункта 3 dict, ключами которого являются слова, а значениями их количество появлений в тексте;
dict_worlds = dict.fromkeys(text)
for word in text:
    q_ty = len(list(filter(lambda x: x == word, text)))
    dict_worlds[word] = q_ty
print(dict_worlds)


# вывести 5 наиболее часто встречающихся слов (sort)
values  =[]
for value in dict_worlds.values():
    values.append(value)
# print(values)
values.sort()
# print(values)
for key, value in dict_worlds.items():
    if value in values[-5:]:
        print(key)


# вывести количество разных слов в тексте (set).
# через ключи
set_keys = set(dict_worlds.keys())
print(set_keys)
print(len(set_keys))

# через текст на основе правил формирования множеств
unique_words = set(text)
# print(set_keys)
print(len(unique_words))