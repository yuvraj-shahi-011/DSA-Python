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
count = 0
current = head
while current is not None:
    count += 1
    current = current.next
print("Number of nodes:", count)