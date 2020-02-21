{\rtf1\ansi\ansicpg1252\cocoartf2511
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs26 \cf0 \expnd0\expndtw0\kerning0
#QuickSort\
import time\
import random\
import matplotlib.pyplot as plt\
tempos=[]\
\
def geraVetor(tam):\
    vetor = list(range(tam,0,-1))\
    return vetor\
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
for i in vetor:\
  antes=time.time()\
  quick_sort(geraVetor(i),0,i-1)\
  depois=time.time()\
  tempos.append(depois-antes)\
\
plt.plot(vetor,tempos)\
plt.show()}