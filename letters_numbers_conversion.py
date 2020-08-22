
def convert_to_numbers(input_string):
    numbers = []
    for char in input_string:
        if char != " ":
            numbers.append(ord(char) - 96)
        if char == " ":
            numbers.append(0)
    return numbers
print('testing convert_to_numbers on input "batman"...')
assert convert_to_numbers("batman") == [2, 1, 20, 13, 1, 14], 'Test Failed'
print("PASSED")

def convert_to_letters(input_string):
    string = ""
    for number in input_string:
        if number != 0:
            string += chr(number + 96)
        if number == 0:
            string += " "
    return string
print('testing convert_to_letters on input [1,0,3,1,20]...')
assert convert_to_letters([1, 0, 3, 1, 20]) == "a cat", "Test Failed"
print("PASSED")