def skip_factorial_nonrecursive(n):
    final_product = 1
    if n % 2 == 0:
        for num in range(2, n+2, 2):
            final_product = final_product*num
    else:
        for num in range(1, n+2, 2):
            final_product = final_product*num
    return final_product

print('input 6, nonrecursive')
assert skip_factorial_nonrecursive(6) == 48, "test failed"
print('PASSED')

print('input 7, nonrecursive')
assert skip_factorial_nonrecursive(7) == 105, "test failed"
print('PASSED')


def skip_factorial_recursive(n):
    if n <= 1:
        return 1
    else:
        return n*skip_factorial_recursive(n-2)

print('input 6, recursive')
assert skip_factorial_recursive(6) == 48, "test failed"
print('PASSED')

print('input 7, recursive')

assert skip_factorial_recursive(7) == 105, "test failed"
print('PASSED')
