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

def shell_sort(codigo):

    pulo = len(codigo) // 2
    while pulo > 0:
        i = pulo
        while i < len(codigo):
            global comparacao
            comparacao = comparacao + 1
            temp = codigo[i]
            trocou = False
            j = i - pulo
            while j >= 0 and codigo[j] > temp:
                codigo[j + pulo] = codigo[j]
                trocou = True
                j -= pulo

            if trocou:
                codigo[j+pulo] = temp

            i += 1
        pulo = pulo // 2

random.shuffle(codigo) #Embaralha o código
inicio = time.time()
shell_sort(codigo)
final = time.time()
total = (final - inicio) * 1000

print("Comparações: ",comparacao)
print("Tempo total: %0.2f ms" %total)
print(codigo)

