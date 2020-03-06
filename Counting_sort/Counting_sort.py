#COUNTINGSORT
import time
import random
import matplotlib.pyplot as plt
tempos=[]

def geraVetor(tam):
    vetor = list(range(tam,0,-1))
    random.shuffle(vetor)
    return vetor

def sort(vetor, maximo):
    antes=time.time()
    count(vetor, maximo)
    depois=time.time()
    return (depois-antes)

def count(vetor, maximo):
  count = [0] * (maximo+1)
  vetorOrdenada = [None] * len(vetor)
  for i in range(len(vetor)):
    count[vetor[i]] += 1
  for i in range(1, maximo+1):
    count[i] += count[i-1]
  for i in range(len(vetor)):
    vetorOrdenada[count[vetor[i]]-1] = vetor[i]
    count[vetor[i]] -= 1
  
  
vetor = [30000,40000,50000,60000,70000]

for i in range(len(vetor)):
  tempo=sort(geraVetor(vetor[i]),vetor[i])
  tempos.append(tempo)

plt.plot(vetor,tempos)
plt.show()
