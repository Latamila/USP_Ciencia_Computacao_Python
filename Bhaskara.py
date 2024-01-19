import math

a = int(input('insira o valor de a: '))
b = int(input('insira o valor de b: '))
c = int(input('insira o valor de c: '))

delta = (b**2)-4*a*c

if delta < 0:
  print('esta equação não possui raízes reais')
else:
  X = (-(b) + math.sqrt(delta))/(2*a)
  Y = (-(b) - math.sqrt(delta))/(2*a)
  if delta == 0:
    print(f'a raiz desta equação é {X}')
  else:
    if X < Y:
      Y = (-(b) - math.sqrt(delta))/(2*a)
      print(f'as raízes da equação são {X} e {Y}')
    else:
