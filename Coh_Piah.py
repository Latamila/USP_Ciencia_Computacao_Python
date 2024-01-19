import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


def novas_palavras(list):
  palavras = []
  sentencas = separa_sentencas(list)
  for sentenca in sentencas:
    novas_frases = separa_frases(sentenca)
    for frase in novas_frases:
      palavras.extend(separa_palavras(frase))
  return palavras


def hapax(str):
  palavras = novas_palavras(str)
  hapax = n_palavras_unicas(palavras)/len(palavras)
  return hapax


def type_token(str):
  palavras = novas_palavras(str)
  type_token = n_palavras_diferentes(palavras)/len(palavras)
  return type_token


def media_palavras(str):
  soma = 0
  palavras = novas_palavras(str)
  for palavra in palavras:
    tamanho = len(palavra)
    soma += tamanho

  tamanho_medio = soma/len(palavras)
  return tamanho_medio



def media_sentencas(str):
  soma = 0
  sentencas = separa_sentencas(str)
  for sentenca in sentencas:
    contagem = len(sentenca)
    soma += contagem
  media_total = soma/len(sentencas)
  return media_total


#Numero total de frases dividido pelo número de sentenças.
def media_complexidade(str):
  soma = 0
  sentencas = separa_sentencas(str)
  for sentenca in sentencas:
    frases =separa_frases(sentenca)
    for frase in frases:
      soma += 1
  tamanho_sentenca = len(sentencas)
  media_complexidade = soma / len(sentencas)
  return media_complexidade


#Média simples do numero de caracteres por FRASE
#Tamanho médio de frase é a soma do número de
#caracteres em cada frase dividida pelo número de frases no texto

def media_frase(str):
    soma = 0
    total_frases = 0
    sentencas = separa_sentencas(str)
    for sentenca in sentencas:
      frases =separa_frases(sentenca)
      for frase in frases:
        total_frases += 1
        tamanho = len(frase)
        soma += tamanho
    media_total = soma / total_frases
    return media_total


def calcula_assinatura(list):
  i = len(list)
  assinatura = []
  assinatura.append(media_palavras(list))
  assinatura.append(type_token(list))
  assinatura.append(hapax(list))
  assinatura.append(media_sentencas(list))
  assinatura.append(media_complexidade(list))
  assinatura.append(media_frase(list))
  return assinatura


def assinaturas(list):
  assinaturas = []
  for i in range(len(list)):
    assinaturas.append(calcula_assinatura(list[i]))
  return assinaturas



def compara_assinatura(as_a,as_b):
  i = 0
  soma = 0 
  similarity = 0
  while i <= 5:
    soma_dif = 0
    dif = abs(as_a[i])-abs(as_b[i])
    soma += abs(dif)
    i += 1
  similarity = soma / 6
  return similarity




def avalia_textos(list, ass_cp):
  menor_ponto = 100.0
  contador = 0
  i = 0
  as_b = le_assinatura()
  while i < len(list):
    for texto in list:
      ass = assinaturas(list)
      a = ass[i]
      i += 1
      as_a = a
      comparado = compara_assinatura(as_a,as_b)
      if comparado < menor_ponto:
        menor_ponto = comparado
        contador += 1
    return contador



def main():
  print('Bem-vindo ao detector automático de COH-PIAH')
  print('Informe a assinatura típica de um aluno infectado: ')
  ass_cp= le_assinatura()
  print(ass_cp)
  textos = le_textos()
  print(f'O autor do texto {avalia_textos(textos,ass_cp)} está infectado com COH-PIAH')

main()
