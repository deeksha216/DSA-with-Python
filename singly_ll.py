class node:
    def __init__(self, data):
        self.data=data
        self.next=None
class singlylinkedlist:
    def __init__(self):
        self.head=None

    def insert(self,data):
        new_node=node(data)
        new_node.next=self.head
        self.head=new_node

    def append(self,data):
        new_node=node(data)
        if self.head is None:
            self.head=new_node
            return
        current=self.head
        while current.next:
            current=current.next
        current.next=new_node

    def insert_at_position(self,data,position):
        if position<1:
            print("position must be >=1")
            return
        new_node=node(data)
        if position==1:
            new_node.next=self.head
            self.head=new_node
            return
        current=self.head
        count=1
        while current is not None and count<position -1:
            current=current.next
            count+=1
        if current is None:
            print("position out of range")
            return
        new_node.next=current.next
        current.next=new_node

    def traverse(self):
        if self.head is None:
            print("linked list is empty")
            return
        current=self.head
        while current:
            print(current.data,end="->")
            current=current.next
        print("none")

l=singlylinkedlist()
l.append(18)
l.insert_at_position(25,1)
l.traverse()
