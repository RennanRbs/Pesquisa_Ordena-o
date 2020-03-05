# MergeSort

import time
import random
import matplotlib.pyplot as plt

tempos = []


def geraVetor(tam):
    vetor = list(range(tam, 0, -1))
    random.shuffle(vetor)
    return vetor


def shell_sort(vetor):
    antes = time.time()
    tamanho = len(vetor)
    intervalo = tamanho // 2

    while intervalo > 0:
        for i in range(intervalo, tamanho):
            aux = vetor[i]
            j = i
            while j >= intervalo and vetor[j - intervalo] > aux:
                vetor[j] = vetor[j - intervalo]
                j -= intervalo
            vetor[j] = aux
        intervalo //= 2
    depois = time.time()
    return (depois - antes)


def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the array elements
        R = arr[mid:]  # into 2 halves

        mergeSort(L)  # Sorting the first half
        mergeSort(R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


# Code to print the list
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


# driver code to test the above code
    if __name__ == '__main__':
        tam = [30000, 40000, 50000, 60000, 70000]

        for i in range(len(vetor)):
            tempo = shell_sort(geraVetor(vetor[i]))
            tempos.append(tempo)

    plt.plot(vetor, tempos)
    plt.show()
