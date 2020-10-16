class Node():

    def __init__(self, data = None):
        self.data = data
        self.next = None
        self.index = 0

class LinkedList():
    def __init__(self, head):
        self.head = Node(head)
    
    def print_data(self):
        print_val = self.head
        while print_val is not None:
            print(print_val.data)
            print_val = print_val.next
    
    def length(self):
        N_head = self.head
        length = 0
        while N_head is not None:
            length += 1
            N_head = N_head.next
        return length
    
    def append(self, number):
        new_node = self.head
        node_index = 0
        while new_node.next is not None:
            new_node = new_node.next
            node_index += 1
        node_index += 1
        new_node.next = Node(number)
        new_node.next.index = node_index

    def push(self, new_data):
        previous_head = self.head
        self.head = Node(new_data)
        self.head.next = previous_head
        self.head.index = 0
        new_node = self.head
        
        while new_node.next is not None:
            new_node.next.index += 1
            new_node = new_node.next

    def get_node(self, index):
        new_node = self.head
        for number in range(index):
            new_node = new_node.next
        return new_node

    def delete(self, index):
        current_head = self.head
        if index == 0:
            self.head = current_head.next
            current_head = None
            return 
        for previous_node in range(index - 1):
            current_head = current_head.next
            if current_head == None:
                break
        next = current_head.next.next
        current_head.next = None
        current_head.next = next

    def insert(self, new_data, index):
        new_node = Node(new_data)
        previous_node = self.get_node(index - 1)
        current_node = self.get_node(index)
        previous_node.next = new_node
        new_node.next = current_node
        new_node.index = index
        loop_node = new_node
        while loop_node.next != None:
            loop_node.next.index += 1
            loop_node = loop_node.next




A = Node(4)
assert A.data == 4, 'test failed'
print('PASSED')

assert A.next == None, 'test failed'
print('PASSED')

B = Node(8)
A.next = B
assert A.next.data == 8, 'test failed'
print('PASSED')

linked_list = LinkedList(4)
assert linked_list.head.data == 4, 'test failed'
print('PASSED')

linked_list.append(8)
assert linked_list.head.next.data == 8, 'test failed'
print('PASSED')

linked_list.append(9)
linked_list.print_data()

assert linked_list.length() == 3, 'test failed'
print('PASSED')

linked_list = LinkedList('b')
linked_list.append('e')
linked_list.append('f')
linked_list.push('a')
assert linked_list.length() == 4
print('PASSED')

assert linked_list.head.index == 0
print('PASSED')
assert linked_list.head.next.index == 1
print('PASSED')
assert linked_list.head.next.next.index == 2
print('PASSED')
assert linked_list.head.next.next.next.index == 3
print('PASSED')

print('testing "get_node"...')
assert linked_list.get_node(0).data == 'a'
print('PASSED')
assert linked_list.get_node(1).data == 'b'
print('PASSED')
assert linked_list.get_node(2).data == 'e'
print('PASSED')
assert linked_list.get_node(3).data == 'f'
print('PASSED')

linked_list = LinkedList('a')
linked_list.append('b')
linked_list.append('c')
linked_list.append('d')
linked_list.append('e')
assert linked_list.length() == 5
print('testing length = 5')
print('PASSED')
print(linked_list.print_data())

assert linked_list.get_node(2).data == 'c'
print('PASSED')

linked_list.delete(2)

assert linked_list.length() == 4
print('PASSED')
assert linked_list.get_node(2).data == 'd'
print('PASSED')
linked_list.print_data()

linked_list.insert('f', 2)
assert linked_list.length() == 5
print('PASSED')
assert linked_list.get_node(2).data == 'f'
print('PASSED')
print(linked_list.print_data())
