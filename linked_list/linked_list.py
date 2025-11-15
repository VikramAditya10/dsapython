class Node:
    def __init__(self,data):
        self.data = data
        self.next=None
    

class LinkedList:
    def __init__(self):
        self.head = None

    def add_at_begining(self, data):
            self.head = Node(data)
            self.head.next = None
    def add(self, data):
        if self.head is None:
            self.add_at_begining(data)
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            node = Node(data)
            current_node.next=node

    def print_list(self):
        current_node = self.head.next
        str = f"{self.head.data}"
        while current_node:
            str=f"{str}->{current_node.data}"
            current_node = current_node.next
        print(str)

    def search(self, data):
        if self.head is None:
            print("Linked List empty")
            return
        position = 1
        current_node = self.head
        while current_node:
            if current_node.data == data:
                print(f"Found data at position {position}")
                return
            else:
                current_node=current_node.next
            position+=1

        print("Couldn't find element")


    def delete_from(self,position):
        if self.head is None:
            print("Empty linked list")
            return
        if position == 1:
            self.head = self.head.next
            return
        counter=1
        prev_node = self.head
        current_node=self.head.next
        while current_node:
            if counter==position:
                prev_node.next = current_node.next
                return
            prev_node=current_node
            current_node=current_node.next
            counter+=1

        if position>counter:
            print("Invalid position")

    def add_to_position(self,position,data):
        if position>1 and self.head is None:
            print("Invalid position")
        if position == 1:
            node  = Node(data)
            node.next = self.head
            self.head = node            
        prev_node = self.head
        current_node = prev_node.next
        




ll = LinkedList()
ll.add(11)
ll.add(2)
ll.add(19)
ll.add(54)
ll.print_list()
ll.search(19)
ll.search(10)
ll.delete_from(1)
ll.print_list()
ll.delete_from(10)
ll.add_to_position(1,10)
ll.print_list()
