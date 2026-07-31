queue = []
n = int(input("How many elements do you want to enqueue? "))
for i in range(n):
    element = input("Enter element: ")
    queue.append(element)
print("Queue:", queue)