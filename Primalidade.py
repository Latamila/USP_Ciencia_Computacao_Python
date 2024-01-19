n = int(input('primo ou nao primo: '))

if n ==1 or n == 2 or n == 3 or n==7:
  print('primo')
else:
  for i in range(2, n):
    if n%i == 0:
      print('não primo')
      break
    else:
      if i == n-1:
        print('primo')
