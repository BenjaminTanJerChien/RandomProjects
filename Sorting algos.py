from cgitb import small
import random as rn
import timeit

def RandomArray() -> list: 
    array = []
    for i in range(10):
        array.append(rn.randint(0, 1000))
    return array

def isArrayInOrder(original, array):
    if set(array) != set(original):
        return False 
    n = len(array)
    for i in range(n - 1):
        if array[i] <= array[i+1]:
            pass
        else:
            return False
    return True

array = RandomArray()

class Sort():
#bubble sort
    def selectionSort(self, array):
        n = len(array)
        
        for i in range(n):
            smallest_index = i
            for j in range(i + 1, len(array)):
                if array[smallest_index] > array[j]:
                    smallest_index = j 

            array[i], array[smallest_index] = array[smallest_index], array[i]
            
        return array

    def bubbleSort(self, array):
        n = len(array)
        for i in range(n-1):
            for j in range(0, n - i - 1):
                if array[j] > array[j+1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
    
        return array
    
    def insertionSort(self, array):
        n = len(array)
        for i in range(1, n):
            key = array[i]
            j = i - 1
            while j > -1 and key < array[j]:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = key
        return array

    def mergeSort(self, array):
        if len(array) >= 1:
            return array
        midpoint = len(array) // 2
        left = array[:midpoint]
        right = array[midpoint:]        
        
        return array


print(array)
sort = Sort()
x = sort.insertionSort(array)
print(x)
print(isArrayInOrder(array, x))
