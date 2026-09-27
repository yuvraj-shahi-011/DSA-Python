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
data = int(input("Enter element: "))
position = int(input("Enter position: "))
new_node = Node(data)
if position == 1:
    new_node.next = head
    head = new_node
else:
    current = head
    for i in range(position - 2):
        if current is None:
            break
        current = current.next
    if current is None:
        print("Invalid position")
    else:
        new_node.next = current.next
        current.next = new_node
print("Linked List:")
current = head
while current is not None:
    print(current.data, end=" -> ")
    current = current.next
print("None")