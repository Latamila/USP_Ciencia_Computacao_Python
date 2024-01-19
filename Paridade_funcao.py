def multiplode2():
  if i%2 != 0:
    return i


def multiplode3(list):
  if list[i]%3 != 0:
    return list[i]

def multiplode5(list):
  if list[i]% 5 != 0:
    return list[i]

def multiplode7(list):
  if list[i]% 7 != 0:
    return list[i]

p_lista = []
for i in range(2,961):
  p_lista.append(multiplode2())

listasem2 = []
for item in p_lista:
    if item is not None:
        listasem2.append(item)

listasem3=[]
for i in range(len(listasem2)):
  listasem3.append(multiplode3(listasem2))

lista3 = []
for item in listasem3:
    if item is not None:
        lista3.append(item)

list3=[]
for i in range(len(lista3)):
  list3.append(multiplode5(lista3))

listasem5 = []
for item in list3:
    if item is not None:
        listasem5.append(item)

listpara7=[]
for i in range(len(listasem5)):
  listpara7.append(multiplode7(listasem5))

listasem7 = []
for item in listpara7:
    if item is not None:
        listasem7.append(item)

print(listasem7[-1])
