a = float(input('Введите год: '))
if a % 4 == 0 and a % 100 != 0:
  print('Год високосный')
elif a % 400 == 0:
  print('Год високосный')
else:
  print('Год не високосный')