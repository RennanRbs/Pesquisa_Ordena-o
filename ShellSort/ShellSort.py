# MergeSort

import time
import random
# import matplotlib.pyplot as plt

tempos = []
def geraVetor(tam):
    vetor = list(range(tam,0,-1))
    return vetor


def shellSort(arr):
    # Start with a big gap, then reduce the gap
    n = len(arr)
    gap = n / 2

    # Do a gapped insertion sort for this gap size.
    # The first gap elements a[0..gap-1] are already in gapped
    # order keep adding one more element until the entire array
    # is gap sorted
    while gap > 0:

        for i in range(gap, n):

            # add a[i] to the elements that have been gap sorted
            # save a[i] in temp and make a hole at position i
            temp = arr[i]

            # shift earlier gap-sorted elements up until the correct
            # location for a[i] is found
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

                # put temp (the original a[i]) in its correct location
            arr[j] = temp
        gap /= 2

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
    numerosDosVetores = [30000,40000,50000,60000,70000,80000]
    arr = geraVetor(numerosDosVetores)
    print("Given array is", end="\n")
    printList(arr)
    shellSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)

    # for i in numerosDosVetores:
    #         antes = time.time()
    #         shellSort(geraVetor(i))
    #         depois = time.time()
    #         tempos.append(depois - antes)
    #
    # plt.plot(numerosDosVetores, tempos)
    # plt.show()