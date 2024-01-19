#função vogal recebe um unico caractere que devolve
#true se ele for uma vogal e false se for uma consoante

def vogal(string):
  v = string.lower()
  if v == 'a' or v == 'e' or v == 'i' or v == 'o' or v == 'u':
    return True
  else: 
    return False
