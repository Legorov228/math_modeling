a = int(input('Введите первый коэффициент: '))
b = int(input('Введите второй коэффициент: '))
c = int(input('Введите третий коэффициент: '))

if D > 0:
  f = b ** 2 - 4 * a * c
  x1 = (-b + math.sqrt(f)) / (2 * a)
  x2 = (-b - math.sqrt(f)) / (2 * a)
  print(f'Первый корень: {x1}')
  print(f'Второй корень: {x2}')
  if D = 0:
    x = -b / (2 * a)
    print(f'Один корень: {x}')
  else:
    print('Нет корней!')