def identity_matrix_elements(n):
    return [[(int(i == j)) for j in range(n)] for i in range(n)]

assert identity_matrix_elements(4) == [[1, 0, 0, 0],
 [0, 1, 0, 0],
 [0, 0, 1, 0],
 [0, 0, 0, 1]], 'test failed'
print('PASSED')

def counting_across_rows_matrix_elements(m,n):
    return [[(1 + j + i*n) for j in range(n)] for i in range(m)]

print('Testing counting_across_rows_matrix_elements(3,4)')
assert counting_across_rows_matrix_elements(3,4) == [[1, 2, 3, 4],
 [5, 6, 7, 8],
 [9, 10, 11, 12]], 'test failed'
print('PASSED')