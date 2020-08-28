class Stack():
    data = []
    def __init__(self):
        self.data = [] 


    def push(self, string):
        self.data.append(string)


    def pop(self):
        self.data.pop()


    def peek(self):
        return self.data[-1]

s = Stack()

print(">>> s = Stack()")
print(">>> Test 1")
assert s.data == [], "Test Failed"
print("PASSED")

print(">>> Test 2")
s.push('a')
s.push('b')
s.push('c')
assert s.data == ['a', 'b', 'c'], "Test Failed"
print("PASSED")

print(">>> Test 3")
s.pop()
assert s.data == ['a', 'b'], "Test Failed"
print("PASSED")

print(">>> Test 4")
s.peek()
assert s.peek() == 'b', "Test Failed"
print("PASSED")

print(">>> s.data")
print(">>> Test 5")
assert s.data == ['a', 'b'], "Test Failed"
print("PASSED")
