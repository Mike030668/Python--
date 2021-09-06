sample_list = ["мандаринки", "киви", "лимон"]
n=int(input('введите натуральное число'))
a_list=[]
for i in range(n):
 a_el='_'+str(i+1)
 a_list.append(a_el)
new_list=[]
for k in range(len(a_list)):
  for j in range(len(sample_list)):
    new_el=str(sample_list[j])+str(a_list[k])
    new_list.append(new_el)
print('Сгенерированный  лист:')
print(new_list)
