def ar_func(*args):
  i = 0
  s = 1
  while i < len(args):
    s = s * args[i]
    i = i + 1
  print(s)

ar_func(3, 4, 5, 185)