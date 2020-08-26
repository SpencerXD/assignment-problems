def first_n_terms(n):
    final_list = []
    for num in range(1, n): 
        if num == 1:
            basecase = 5
            final_list.append(5)
        final_list.append(3*basecase - 4)
        basecase = 3*basecase - 4
    return final_list
print(">>> first_n_terms(10)")
assert first_n_terms(10) ==  [5, 11, 29, 83, 245, 731, 2189, 6563, 19685, 59051], "Test Failed"
print("PASSED")

def nth_term(n): 
    if n == 1:
        return 5
    return 3*nth_term(n-1) - 4
print(">>> nth_term(10)")
assert nth_term(10) == 59051, "Test Failed"
print("PASSED")