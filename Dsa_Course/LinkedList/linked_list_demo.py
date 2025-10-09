class Node:
    def __init__(self,data):
        self.data = data
        self.pointer = None      

#Creating Node
first_node = Node(10)
second_node = Node(20)

#Assigning second addres to firts pointer
first_node.pointer = second_node

#Assigning firts node as Head
head = first_node

#Strat from Head
current = head

while current: #Address is not None
    print('Data : ',current.data , '| Pointer : ' , current.pointer)
    current = current.pointer #Point the value to next address

# # Step 5: Print values
# print("First node data:", head.data) #Fisrt Node Value     # 10
# print("Second node data:", head.pointer.data) #Fisrt Node -> Address(2nd Node) ->@nd Node Value     # 20
# print("Next of second node:", head.pointer.pointer) # Firts Node -> Address(2nd Node) ->Address of 2nd Node # None