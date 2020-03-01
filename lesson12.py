x = 2

if x:
    print('Выражение ИСТИНО')

else:
    print('Выражение ЛОЖНО')

light = 'green'

if light == 'red':
    print('Stop')
elif light == 'yellow':
    print('Wait')
elif light == 'green':
    print('Go')

# age = int(input("Введите ваш возраст"))
# if age>= 18:
#     print('Добро пожаловать')
# else:
#     print('Вам еще рано')
#     print(f'Вам не хватает {18 - age} лет')

time = 11
day = 'st'

if time < 12 or time > 13 and day != 'su':
    print('Open')
else:
    print('Close')

a = 0

if not x:
    print("OK")
else:
    print('NO')

res = 'OK' if x else 'NO' # Сокращенная запись