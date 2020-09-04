class Queue():
    data = []

    def enqueue(self, string):
        self.data.append(string)
    
    def dequeue(self):
        self.data.pop(0)
    
    def peek(self):
        return self.data[0]
q = Queue()

print('Testing q.data')
assert q.data == [], 'Test Failed'
print('PASSED')


q.enqueue('a')
q.enqueue('b')
q.enqueue('c')
print('Testing enqueue')
assert q.data == ['a', 'b', 'c'], 'Test Failed'
print('PASSED')


q.dequeue()
print('Testing dequeue')
assert q.data == ['b', 'c'], 'Test Failed'
print('PASSED')

print('Testing dequeue')
assert q.peek() == 'b', 'Test Failed'
print('PASSED')

print('Testing peek')
assert q.data == ['b', 'c'], 'Test Failed'
print('PASSED')