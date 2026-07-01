n = int(input("Enter number of elements: "))

arr = list(map(int, input("Enter elements: ").split()))

smallest = arr[0]

for i in arr:
    if i < smallest:
        smallest = i

print("Smallest element is:", smallest)