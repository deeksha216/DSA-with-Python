class node:
    def __init__(self, data):
        self.data = data
        self.prev=None
        self.next=None
class doublylinkedlist:
    def __init__(self):
        self.head=None
    def insert_at_beginning(self,data):
        new_node=node(data)
        if self.head is None:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
    def insert_at_end(self,data):
        new_node=node(data)
        if self.head is None:
            self.head=new_node
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node
        new_node.prev=temp
    def insert_at_position(self,data,pos):
        if pos<=0:
            print("position should be >=1")
            return
        new_node=node(data)
        if pos==1:
         self.insert_at_beginning(data)
         return
        temp=self.head
        count=1
        while temp and count<pos-1:
            temp=temp.next
            count+=1
        if temp is None:
            print("position out of range")
            return
        new_node.next=temp.next
        new_node.prev=temp
        if temp.next:
            temp.next.prev=new_node
        temp.next=new_node
    def display_forward(self):
        temp=self.head
        while temp:
            print(temp.data,end="<->")
            temp=temp.next
        print("none")

dll=doublylinkedlist()
dll.insert_at_end(10)
dll.insert_at_end(20)
dll.insert_at_end(30)
dll.insert_at_beginning(5)  
dll.insert_at_position(15,3)
print("forward traversal:")
dll.display_forward()
