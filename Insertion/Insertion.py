import time
import random
import matplotlib.pyplot as plt
tempos=[]

def geraVetor(tam):
    vetor = list(range(tam,0,-1))
    random.shuffle(vetor)
    return vetor

def insertion_sort(vetor):
    antes=time.time()
    count = 0
    for x in range(0, len(vetor)):
        a = vetor[x]
        y = x-1
        while a < vetor[y] and y>=0:
            vetor[y+1] = vetor[y]
            y-=1
            count+=1
        vetor[y+1] = a
        count+=1
        depois=time.time()
    
    return (depois-antes)
  
vetor = [1000,10000,30000,60000]

for i in range(len(vetor)):
  tempo=insertion_sort(geraVetor(vetor[i]))
  tempos.append(tempo)


plt.plot(vetor,tempos)
plt.show()
