def eh_primo(x):
  fator = 2
  while x % fator != 0 and fator < (x/2):#nao preciso ir
  #até x. até a metade basta para encontrar um divisor
    fator = fator + 1
  if x == 2:
    return True
  elif x % fator == 0:
    return False
  else:
    return True

def n_primos(n):
  cont = 0
  for i in range(2,n+1):
    if eh_primo(i):
      cont=cont+1
  return cont
