# комментарий
'''
много комментария
и еще
'''

print('Типы переменных')

print('1.')
# марка
name = 'ford'
print(name, type(name), end='\n')

print('2.')
# возраст в целых
age = 3
print(age, type(age), end='\n')

print('3.')
# объем двиателя
engine_volume = 1.6
print(engine_volume, type(engine_volume), end='\n')

print('4.')
# есть ли что-то
sky_frame = False
print(sky_frame, type(sky_frame), end='\n')

###################

age = input('сколько тебе лет?')
age = int(age)
my_age = 23
print('А мне', str(my_age))
print('Значит нам вместе', my_age+age)

###################

a = int(input('введите число a '))
b = int(input('введите число b '))

print('a + b = ', a+b, ' ', type(a+b))
print('a - b = ', a-b, ' ', type(a-b))
print('a * b = ', a*b, ' ', type(a*b))
print('a / b = ', a/b, ' ', type(a/b))
print('a / b = ', a//b, ' ', type(a//b))
print('a = b ? ', a == b, ' ', type(a == b))
