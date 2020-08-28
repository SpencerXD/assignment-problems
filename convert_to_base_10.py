def convert_to_base_10(binary):
    decimal = 0
    binary = list(str(binary))
    binary = binary[::-1]
    power = 0
    for num in binary:
        if num == "1":
            decimal += 2**power
        power += 1
    return decimal
print(">>> convert_to_base_10(10011)")
assert convert_to_base_10(10011) == 19, "Test Failed"
print("PASSED")
