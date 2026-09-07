size = int(input("Enter queue size: "))
queue = []
while True:
    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        if len(queue) == size:
            print("Queue is Full")
        else:
            queue.append(input("Enter element: "))
    elif choice == 2:
        if len(queue) == 0:
            print("Queue is Empty")
        else:
            print("Removed:", queue.pop(0))
    elif choice == 3:
        print(queue)
    elif choice == 4:
        break