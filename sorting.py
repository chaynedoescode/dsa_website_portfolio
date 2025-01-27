import numpy as np

# • Bubble sort
# • Selection sort
# • Insertion sort
# • Merge sort
# • Quicksort 

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        print(f'Pass {i+1}: {arr}')

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(f'Pass {i+1}: {arr}')

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(f'Pass {i}: {arr}')

def merge_sort(arr):
    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def merge_sort_recursive(arr, depth=0):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = merge_sort_recursive(arr[:mid], depth+1)
        right = merge_sort_recursive(arr[mid:], depth+1)
        merged = merge(left, right)
        print(f'Pass {depth}: {merged}')
        return merged

    return merge_sort_recursive(arr)

def quicksort(arr):
    def quicksort_recursive(arr, low, high, depth=0):
        if low < high:
            pi = partition(arr, low, high)
            print(f'Pass {depth}: {arr}')
            quicksort_recursive(arr, low, pi-1, depth+1)
            quicksort_recursive(arr, pi+1, high, depth+1)

    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return i+1

    quicksort_recursive(arr, 0, len(arr) - 1)
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
print(f'Original: {arr}\n')
print(f"Bubble sort\n {bubble_sort(arr.copy())}\n")
print(f"Selection Sort\n {selection_sort(arr.copy())}\n")
print(f"Insertion Sort\n {insertion_sort(arr.copy())}\n")
print(f"Merge Sort\n {merge_sort(arr.copy())}\n")
print(f"Quicksort\n {quicksort(arr.copy())}\n")

