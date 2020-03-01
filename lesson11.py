# Форматирование строк
name = 'Nik'
age = 32
#print('My name is %(name)s and i\'m %(age)d' % {'name': name, 'age':age})
print('My name is %s and i\'m %d' %(name, age))
# Функция формат

print('My name is {} and i\'m {}' .format(name, age))
print('My name is {0} and i\'m {1}' .format(name, age)) #My name is Nik and i'm 32
print('My{0} name is {0} and i\'m {1}' .format(name, age)) #MyNik name is Nik and i'm 32
print('My name is {name} and i\'m {age}'.format(name=name, age=age)) #My name is Nik and i'm 32

#f - strings - Ф строки
print(f'My name is {name} and i\m {age + 5}') #My name is Nik and i\m 37
print(f'5 + 2 = {5 + 2}') #5 + 2 = 7