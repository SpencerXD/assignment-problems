
def is_symmetric(input_string):
    if input_string == input_string[::-1]:
        symmetry = True 
    else: 
        symmetry = False

    return symmetry

print("testing is_symmetric on input 'racecar'...")
assert  is_symmetric("racecar") is True, "racecar Test Failed"
print("PASSED")

print("testing is_symmetric on input 'batman'...")
assert is_symmetric("batman") is False, "batman Test Failed"
print("PASSED")
