def ar_func(*args):
  i = 0
  s = 0
  while i < len(args):
    s = s + args[i]
    i = i + 1
  print(s/len(args))

ar_func(3, 4, 8, 9)