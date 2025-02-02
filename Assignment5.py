import time
import random
from tabulate import tabulate
import sys

# Adjust recursion limit for larger datasets
sys.setrecursionlimit(2000000)

def standard_quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot_element = arr[0]
    left_partition = [item for item in arr[1:] if item <= pivot_element]
    right_partition = [item for item in arr[1:] if item > pivot_element]

    return standard_quicksort(left_partition) + [pivot_element] + standard_quicksort(right_partition)

def randomized_quick_sort(arr, low, high):
    if low < high:
        pivot_index = shuffle_partition(arr, low, high)
        randomized_quick_sort(arr, low, pivot_index - 1)
        randomized_quick_sort(arr, pivot_index + 1, high)

def partition_using_first_element(arr, low, high):
    # Select the first element as the pivot
    pivot_value = arr[low]
    i = low + 1
    for j in range(low + 1, high + 1):
        if arr[j] < pivot_value:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[low], arr[i - 1] = arr[i - 1], arr[low]
    return i - 1

def shuffle_partition(arr, low, high):
    rand_index = random.randint(low, high)
    arr[low], arr[rand_index] = arr[rand_index], arr[low]  # Swap chosen pivot with the first element
    return partition_using_first_element(arr, low, high)

def calculate_time(sort_algorithm, arr, *args):
    start = time.perf_counter()
    sort_algorithm(arr, *args)
    return time.perf_counter() - start

def create_dataset(size, pattern_type):
    if pattern_type == 'sorted':
        return list(range(size))
    elif pattern_type == 'reverse_sorted':
        return list(range(size, 0, -1))
    elif pattern_type == 'random':
        return [random.randint(0, size) for _ in range(size)]
    elif pattern_type == 'repeated':
        return [random.randint(0, 10) for _ in range(size)]  # Dataset with duplicate values

sizes = [100, 1000, 10000]
patterns = ['sorted', 'reverse_sorted', 'random', 'repeated']

metrics = []

for size in sizes:
    for pattern in patterns:
        dataset = create_dataset(size, pattern)
        quicksort_time = calculate_time(standard_quicksort, dataset.copy())
        randomized_quicksort_time = calculate_time(randomized_quick_sort, dataset.copy(), 0, len(dataset) - 1)
        metrics.append([size, pattern, quicksort_time, randomized_quicksort_time])

table_headers = ["Dataset Size", "Pattern Type", "Quicksort Time (seconds)", "Randomized Quicksort Time (seconds)"]
print(tabulate(metrics, headers=table_headers, floatfmt=".6f"))
