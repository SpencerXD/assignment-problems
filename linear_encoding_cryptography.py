alphabet = ' abcdefghijklmnopqrstuvwxyz'


def encode(string, a, b):
    numbers = []
    for char in string:
        if char != " ":
            numbers.append(a*(ord(char) - 96)+b)
        if char == " ":
            numbers.append(a*(0) + b)
    return numbers
print(">>> get_encoding('a cat', 2, 3)")
assert encode("a cat", 2, 3) == [5, 3, 9, 5, 43], 'Test Failed'
print("PASSED")


def decode(numbers, a, b):
    string = ''
    for num in numbers:
        if ((num - b)/a) < 0:
            return False
        if ((num - b)/a) > 26:
            return False
        if int((num - b)/a) != ((num - b)/a):
            return False
        string += alphabet[int((num - b)/a)]
    return string
print('>>> decode([5, 3, 9, 5, 43], 2, 3)')
assert decode([5, 3, 9, 5, 43], 2, 3) == 'a cat', 'Test Failed'
print(decode([5, 3, 9, 5, 43], 2, 3))

print('>>> decode([1, 3, 9, 5, 43], 2, 3)')
assert decode([1, 3, 9, 5, 43], 2, 3) is False, 'Test Failed'
print(decode([1, 3, 9, 5, 43], 2, 3))

print('>>> decode([5, 3, 9, 5, 44], 2, 3)')
assert decode([5, 3, 9, 5, 44], 2, 3) is False, 'Test Failed'
print(decode([5, 3, 9, 5, 44], 2, 3))

message = [377,
 717,
 71,
 513,
 105,
 921,
 581,
 547,
 547,
 105,
 377,
 717,
 241,
 71,
 105,
 547,
 71,
 377,
 547,
 717,
 751,
 683,
 785,
 513,
 241,
 547,
 751]

for a in range(1, 101):
    for b in range(0, 101):
        if decode(message, a, b) is not False:
            print(decode(message, a, b))
