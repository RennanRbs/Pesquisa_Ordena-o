#QuickSort\
import time\
import random\
import matplotlib.pyplot as plt\
tempos=[]\
\
def particao(vetor, ini, fim):\
    pivo = vetor[fim - 1]\
    for i in range(ini, fim):\
        if not vetor[i] > pivo:\
            vetor[ini], vetor[i] = vetor[i], vetor[ini]\
            ini += 1\
    return ini-1\
\
def quick_sort(vetor,ini,fim):\
  count = 0\
  if ini < fim:\
    pivo = escolhe_pivo_aleatorio(vetor, ini, fim)\
    quick_sort(vetor, ini, pivo)\
    quick_sort(vetor, pivo + 1, fim)\
    count+=1\
\
def escolhe_pivo_aleatorio(vetor, ini, fim):\
    rand = random.randrange(ini, fim)\
    vetor[fim - 1], vetor[rand] = vetor[rand], vetor[fim - 1]\
    return particao(vetor, ini, fim)\
  \
vetor = [100000,200000,300000,400000,500000]\
\
 def geraVetor(tam):\
 vetor = list(range(tam,0,-1))\
 return vetor\
\
for i in vetor:\
  antes=time.time()\
  quick_sort(geraVetor(i),0,i-1)\
  depois=time.time()\
  tempos.append(depois-antes)\
\
 def escolhe_pivo_com(vetor, ini, fim):\
 rand = random.randrange(ini, fim)\
 vetor[fim - 1], vetor[rand] = vetor[rand], vetor[fim - 1]\
 return particao(vetor, ini, fim)\
 \
plt.plot(vetor,tempos)\
plt.show()}
