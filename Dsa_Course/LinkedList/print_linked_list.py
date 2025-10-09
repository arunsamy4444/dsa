class Node:
    def __init__(self,data):
        self.data = data
        self.pointer = None 
 
        
values = [10, 20, 30, 40]

head = None
current = None

for val in values: #looping the arr 
    new_node = Node(val) #creating node
    if head is None: #checking head is empty
        head = new_node #if yes,then assign newnode is head node 
        current = new_node 
    else:
        current.pointer = new_node #assigning addres to prev node - 20/address = last node 10
        current = new_node #move current to next node - move to 20
        
        
current = head

while current:
    print("Data:", current.data, "| Pointer:", current.pointer)
    current = current.pointer