def count_characters(str1):
    str2 = str1.lower()
    dict = {}
    for char in str2:
        keys = dict.keys()
        if char in keys:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict
print('>>> countCharacters("A cat!!!")')
assert count_characters('A cat!!!') == {
    'a': 2, 'c': 1, 't': 1, ' ': 1, '!': 3}, 'Test Failed'
print("PASSED")
