class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head_node = None

    def is_empty(self):
        return self.head_node is None

    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head_node = new_node
            return

        current = self.head_node
        while current.next:
            current = current.next

        current.next = new_node

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head_node
        self.head_node = new_node

    def print_list(self):
        current = self.head_node
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


lst = LinkedList()

for i in range(11):
    lst.insert_at_tail(i)
    lst.print_list()


