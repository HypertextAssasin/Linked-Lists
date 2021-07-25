class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    
    def __init__(self):
        self.head = None
        
    def PrintList(self):
        x=self.head
        while (x):
            print(x.data)
            x= x.next
            
list1=[]
list1 = LinkedList()
list1.head = Node(10)
Node2= Node(20)
Node3= Node(30)
Node4= Node(40)

list1.head.next = Node2
Node2.next = Node3
Node3.next = Node4

list1.PrintList()

    
