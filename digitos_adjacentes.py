n = input('digite um numero inteiro: ')
igual = False

for i in range(len(n)-1):
  if n[i] != n[i+1]:
    igual = False
    continue
  else:
    igual = True
    break

if igual == True:
  print('sim')
else:
  print('nao')
