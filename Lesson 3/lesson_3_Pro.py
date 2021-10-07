import gdown
import pymorphy2

# загружаем архив
file_path = 'https://drive.google.com/file/d/15fBsTB1ZU_BzEw5SJmlOMX2uuyi1xN1-/view?usp=sharing'
file_id = str(file_path.split('/')[5:-1][0])
name_file = 'text.txt'
gdown.download('https://drive.google.com/uc?id=' + file_id, name_file, quiet=False)


# Считать/скопировать текст из файла
f = open('text.txt').readlines()
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

morph = pymorphy2.MorphAnalyzer()

lemma_text = []
for word in text:
    lemma = morph.parse(word)[0].normal_form
    lemma_text.append(lemma)

lemma_text

