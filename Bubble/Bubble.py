{\rtf1\ansi\ansicpg1252\cocoartf2511
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs26 \cf0 \expnd0\expndtw0\kerning0
import time\
from random import randint\
import matplotlib.pyplot as plt\
tempos=[]\
def geraVetor(tam):\
    vetor = []\
    while len(vetor) < tam:\
        n = randint(1,tam)\
        if n not in vetor: vetor.append(n)\
    return vetor\
\
def bubbleSort(arr):\
    antes=time.time()\
    count = 0\
    n = len(arr)\
    for i in range(n):\
        for j in range(0, n-i-1):\
            count+=1\
            if arr[j] > arr[j+1] :\
                arr[j], arr[j+1] = arr[j+1], arr[j]\
    depois=time.time()\
    return count,(depois-antes)\
  \
vetor = [1000,10000,30000,60000]\
\
for i in range(len(vetor)):\
  saida,tempo=bubbleSort(geraVetor(vetor[i]))\
  saidaB.append(saida)\
  tempos.append(tempo)\
\
plt.plot(vetor,tempos)\
plt.show()}
