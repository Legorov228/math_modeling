a = int(input('Введите четыре числа: '))

b = a // 1000
c = a // 100 % 10
d = a // 10 % 10
f = a % 10
print(f, d, c, b, sep = '')