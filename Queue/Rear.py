queue = []
n = int(input("Enter number of elements: "))
for i in range(n):
    queue.append(input("Enter element: "))
if len(queue) == 0:
    print("Queue is empty")
else:
    print("Rear element:", queue[-1])