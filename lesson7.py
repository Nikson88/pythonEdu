# test = None Обьявление пустой переменной
# print(test)
x = 1
y = 'ff'
print(x, y)
a, b = (4, 7) # множественное обьявление переменных
print(b, a)
# str(), int(), float(), bool() Приведение типов
x = str(x) # Приведение типа переменной к стринговому значению
print(float(a))
print(type(x))
print(b, float(b))

str1 = 'd'
str2 = ''
print(bool(str1)) # True Если значение у переменой есть то True, если нет то False
print(bool(str2)) # False Если значение у переменой есть то True, если нет то False

num_null = 0
print(bool(num_null)) # False Если число 0 то false, если больше или иеньше 0 то  True
print(bool(a)) # True