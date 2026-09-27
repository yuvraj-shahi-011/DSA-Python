class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
head = None
n = int(input("Enter number of nodes: "))
for i in range(n):
    data = int(input("Enter element: "))
    new_node = Node(data)
    if head is None:
        head = new_node
    else:
        current = head
        while current.next is not None:
            current = current.next
        current.next = new_node
position = int(input("Enter position to delete: "))
if head is None:
    print("Linked List is empty")
elif position == 1:
    print("Deleted:", head.data)
    head = head.next
else:
    current = head
    for i in range(position - 2):
        if current is None:
            break
        current = current.next
    if current is None or current.next is None:
        print("Invalid position")
    else:
        print("Deleted:", current.next.data)
        current.next = current.next.next
print("Linked List:")
current = head
while current is not None:
    print(current.data, end=" -> ")
    current = current.next
print("None")