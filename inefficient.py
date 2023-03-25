# 비효율적인 linked list..
class Node:
    def __init__(self,Item): # def(space bar)__init__(self,data)
        self.Item = Item 
        self.next = None 

head = Node(1) # Node(1) = data =1
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
node = head # Becase if head is move, all linked list gonna lost , so variable node 
while node: # = node is not None
    print(node.Item,end=" ")
    node = node.next # loop 
