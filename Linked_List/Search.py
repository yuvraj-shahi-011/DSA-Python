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
target = int(input("Enter element to search: "))
current = head
position = 1
found = False
while current is not None:
    if current.data == target:
        print("Element found at position:", position)
        found = True
        break
    current = current.next
    position += 1
if not found:
    print("Element not found")