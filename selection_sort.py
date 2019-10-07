import random
import time

"""
Um sistema de cadastramento de peças onde cada peça possui um codigo identificador e precisamos ordernar
esses códigos.
"""

comparacao = 0
codigo = []
for pecas in range(800):
        nomePeca = "NomeDaPeça X[" + str(pecas) + "]"
        codigo.append(pecas)

def selection_sort(codigo): #Recebe um número como parametro
    i = 0
    while i < len(codigo) - 1:
        menor = i
        j = i + 1
        #Procura qual o menor elemento percorrendo a parte não sorteada.
        while j < len(codigo):
          global comparacao
          comparacao = comparacao + 1
          if codigo[j] < codigo[menor]:
                menor = j
          j += 1
        #Verifica se precisa realizar a troca, Caso o menor número seja diferente da posição comparada.
        if menor != i:
            temp = codigo[i]
            codigo[i] = codigo[menor]
            codigo[menor] = temp
        i += 1


random.shuffle(codigo) #Embaralha o código

#Ordena o vetor.
inicio = time.time()
selection_sort(codigo)
final = time.time()
total = (final - inicio) * 1000

print("Comparações: ",comparacao)
print("Tempo total: %0.2f ms" %total)
print(codigo)


