import random
import time
import matplotlib.pyplot as plt

def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)

def partition(arr, low, high):
    p = arr[high]   # pivot element
    i = low - 1     # index of smaller element

    for j in range(low, high):
        if arr[j] <= p:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Test
arr = [5, 8, 1, 2, 6, 3, 9]
print("before sorting:", arr)
quick_sort(arr, 0, len(arr) - 1)
print("after sorting:", arr)

# Time analysis
n_values = [5000, 10000, 15000, 20000, 25000, 30000]
time_taken = []

for n in n_values:
    arr = [random.randint(1, 10000) for _ in range(n)]
    start_time = time.time()
    quick_sort(arr, 0, len(arr) - 1)
    end_time = time.time()
    elapsed = end_time - start_time   # FIXED
    time_taken.append(elapsed)
    
    print(f"n = {n}, time taken = {elapsed:.4f} seconds")  # FIXED

# Plotting
plt.plot(n_values, time_taken, marker='o')
plt.xlabel("Number of elements (n)")
plt.ylabel("Time taken (seconds)")
plt.title("Quick Sort Time Analysis")
plt.grid(True)
plt.show()