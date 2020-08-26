def intersection(input_values_1, input_values_2):
    return input_values_1.intersection(input_values_2)
print(">>> intersection([1,2,'a','b'], [2,3,'a'])")
assert intersection({1,2,'a','b'}, {2,3,'a'}) == {2,'a'} , "Test Failed"
print('PASSED')

def union(input_values_1, input_values_2):
    return input_values_1.union(input_values_2)
print(">>> union([1,2,'a','b'], [2,3,'a'])")
assert union({1,2,'a','b'},{2,3,'a'}) == {1,2,3,'a','b'}, "Test Failed"
print('PASSED')