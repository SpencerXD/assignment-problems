def convert_to_base_2(base_10):
    bin_base_10 = bin(base_10)[2:]
    return int(bin_base_10)
print(">>> convert_to_base_2(19)")
assert convert_to_base_2(19) == 10011, "Test Failed"
print("PASSED")
