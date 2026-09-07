queue = []
n = int(input("Enter number of elements: "))
for i in range(n):
    queue.append(input("Enter element: "))
queue.reverse()
print("Reversed Queue:")
for element in queue:
    print(element)