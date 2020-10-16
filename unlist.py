def unlist_nonrecursive(x):
    while type(x) == list and len(x) == 1:
        x = x[0]
    return x
print('>>> unlist_nonrecursive([[[[1], [2,3], 4]]])')
assert unlist_nonrecursive([[[[1], [2,3], 4]]]) == [[1], [2,3], 4], 'Test Failed'
print('PASSED')

print('>>> unlist_nonrecursive([[[[1]]]])')
assert unlist_nonrecursive([[[[1]]]]) == 1, 'Test Failed'
print('PASSED')

def unlist_recursive(x):
    if type(x) != list or len(x) != 1:
        return x
    else:
        return unlist_recursive(x[0])

print('>>> unlist_recursive([[[[1]]]])')
assert unlist_recursive([[[[1]]]]) == 1, 'Test Failed'
print('PASSED')
print('>>> unlist_recursive([[[[1], [2,3], 4]]])')
assert unlist_recursive([[[[1], [2,3], 4]]]) == [[1], [2,3], 4], 'Test Failed'
print('PASSED')