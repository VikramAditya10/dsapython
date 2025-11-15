class Node:
    def __init__(self, data):
        self.data=data
        self.prev=None
        self.next=None

class DoublyLinkedList:
    def __init__(self):
        self.first=None
        self.last=None
    def add(self,data):
        if self.first is None:
            node = Node(data)
            self.first = node
            self.first.next=None
            self.first.prev=None
        else:
            current_node=self.first
            while(current_node !=None):
                if current_node.next is None:
                    node = Node(data)
                    node.prev = current_node
                    current_node.next=node
                    self.last=node
                    break
                current_node=current_node.next

    def traverse_from_first(self):
        current_node=self.first
        while(current_node):
            print(current_node.data,end=" ")
            current_node=current_node.next

    def traverse_from_last(self):
        current_node=self.last
        while(current_node):
            print(current_node.data,end=" ")
            current_node=current_node.prev
#todo delete and add to first add to last search item get item from a position      

db = DoublyLinkedList()
db.add(7)
db.add(10)
db.add(15)
db.add(20)
db.traverse_from_first()
db.traverse_from_last()
                

        
