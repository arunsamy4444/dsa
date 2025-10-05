class ListNode:
    def __init__(self,data):
        self.data = data
        self.pointer = None
        
# create nodes
node1 = ListNode(10)
node2 = ListNode("hi")
node3 = ListNode(543)
node4 = ListNode(9.07)
node5 = ListNode("last")  # extra value to make it 5

node1.pointer = node2
node2.pointer = node3
node3.pointer = node4
node4.pointer = node5

cur = node1
while cur:
    print(cur.data , end=' -> ')
    cur = cur.pointer
print('None')