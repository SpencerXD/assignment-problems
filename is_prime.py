def is_prime(input_value):
    for m in range (2, input_value):
        if input_value%m == 0:
            check = False
    return True
print("testing is_prime on input 59...")
assert is_prime(59), "Test Failed"
print("PASSED")

print("testing is_prime on input 51...")
assert is_prime(51), "Test Failed"
print("PASSED")
