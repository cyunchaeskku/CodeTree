class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.node_num = 0

    def push_front(self,new_data):
        new_node = Node(new_data)
        if self.head == None: # 비어있었다면
            self.head = new_node
            self.tail = new_node
            new_node.prev = None
            new_node.next = None
        else: # 비어있지 않았다면
            new_node.prev = None
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.node_num += 1

    def push_back(self, new_data):
        new_node = Node(new_data)
        if self.tail == None: #비어있었다면
            self.head = new_node
            self.tail = new_node
            new_node.prev = None
            new_node.next = None
        else:
            new_node.prev = self.tail
            new_node.next = None
            self.tail.next = new_node
            self.tail = new_node
        self.node_num += 1
    
    def pop_front(self):
        if self.head == None:
            print("List is Empty")
        
        elif self.head.next == None:
            target_node = self.head

            self.head = None
            self.tail = None
            self.node_num = 0

            return target_node.data
        else:
            target_node = self.head

            self.head.next.prev = None
            self.head = target_node.next
            target_node.next = None
            self.node_num -= 1

            return target_node.data

    def pop_back(self):
        if self.tail == None:
            print("List is Empty")

        elif self.tail.prev == None:
            target_node = self.tail
            target_node.prev = None
            target_node.next = None
            self.head = None
            self.tail = None
            self.node_num = 0

            return target_node.data
        else:
            target_node = self.tail

            target_node.prev.next = None
            self.tail = target_node.prev
            
            target_node.prev = None
            self.node_num -= 1
            return target_node.data

    def size(self):
        return self.node_num

    def empty(self):
        if self.node_num > 0:
            return 0
        else:
            return 1

    def front(self):
        if self.head == None:
            print("List is Empty")
        else:
            return self.head.data
    
    def back(self):
        if self.tail == None:
            print("List is Empty")
        else:
            return self.tail.data

    

            
N = int(input())
dll = DLL()

for i in range(N):
    command_line = input().split()

    if command_line[0]  == 'push_front':
        dll.push_front(command_line[1])
    if command_line[0] == 'push_back':
        dll.push_back(command_line[1])
    if command_line[0] == 'pop_front':
        print(dll.pop_front())
    if command_line[0] == 'pop_back':
        print(dll.pop_back())
    if command_line[0] == 'size':
        print(dll.size())
    if command_line[0] == 'empty':
        print(dll.empty())
    if command_line[0] == 'front':
        print(dll.front())
    if command_line[0] == 'back':
        print(dll.back())



