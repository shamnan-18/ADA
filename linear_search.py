n = int(input("Enter number of elements: "))
arr = list(map(int, input("enter elelments:").split()))
key = int(input("Enter element to search: "))
found = False
for i in range(n):
    if arr[i] ==key:
        found = True
        print("Element found at index:", i)
        break
    else:
        found = False