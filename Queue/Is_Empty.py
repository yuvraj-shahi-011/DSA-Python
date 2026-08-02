queue = []
choice = input("Add element? (yes/no): ")
if choice.lower() == "yes":
    queue.append(input("Enter element: "))
if len(queue) == 0:
    print("Queue is Empty")
else:
    print("Queue is Not Empty")