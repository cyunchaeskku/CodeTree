class Stack:
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False
        
    def pop(self):
        if not self.is_empty():
            return self.items.pop()


string = list(input().strip())
s = Stack()
for v in string:
    if v == '(':
        s.push(v)
    if v == ')':
        if s.is_empty():
            print("No")
            exit(0)
        else:
            s.pop()

if s.is_empty() == False:
    print("No")
else:
    print("Yes")


# while s.is_empty() == False:
#     print(s.pop())