import time
import random
import matplotlib.pyplot as plt
tempos=[]

def geraVetor(tam):
    vetor = list(range(tam,0,-1))
    random.shuffle(vetor)
    return vetor

def bucketSort(array):
    bucket = []

    for i in range(len(array)):
        bucket.append([])
        
    for j in array:
        index_b = int(10 * j)
        bucket[index_b].append(j)
    
    for i in range(len(array)):
        bucket[i] = sorted(bucket[i])
        
    k = 0
    for i in range(len(array)):
        for j in range(len(bucket[i])):
            array[k] = bucket[i][j]
            k += 1
    return array
  
vetor = [1000,10000,30000,60000]

for i in range(len(vetor)):
  tempo=insertion_sort(geraVetor(vetor[i]))
  tempos.append(tempo)


plt.plot(vetor,tempos)
plt.show()
