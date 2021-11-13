a = int(input('Введите первый член прогрессии: '))
b = int(input('Введите знаменатель прогрессии: '))
c = int(input('Введите количество членов прогрессии: '))

print(a)

for i in range(0, c):
  d = a * b
  print(d)
  a = d