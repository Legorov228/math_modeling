a = int(input('Введите числитель: '))
b = int(input('Введите знаменатель: '))

if a >= b:
  print('Делиться на: ', a // b)
  print('Остаток: ', a % b)
elif a < b:
  print('Равно нулю')