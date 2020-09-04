def even_odd_tuples(numbers):
   return [(num, 'even') if num%2 == 0 else (num, 'odd') for num in numbers]
print('>>> even_odd_tuples([1,2,3,5,8,11])')
assert even_odd_tuples([1,2,3,5,8,11]) == [(1,'odd'),(2,'even'),(3,'odd'),(5,'odd'),(8,'even'),(11,'odd')], 'Test Failed'
print('PASSED')

def even_odd_dict(numbers):
   return {num:'even' if num%2 == 0 else 'odd' for num in numbers}
print(">>> even_odd_dict([1,2,3,5,8,11])")
assert even_odd_dict([1,2,3,5,8,11]) == {
    1:'odd',
    2:'even',
    3:'odd',
    5:'odd',
    8:'even',
    11:'odd'
}, 'Test Failed'
print("PASSED")
