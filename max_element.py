n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

max_element = arr[0]

for i in range(1, n):
    if arr[i] > max_element: 
        max_element = arr[i]

print("Maximum element:", max_element)