def nth_term(n):
    if n == 1:
        return 0
    elif n == 2:
        return 3
    else:
        return nth_term(n-1) - 2*nth_term(n-2)

print(nth_term(3))

def separate_into_words(string):
    final_list = []
    final_list = string.split(' ')
    return final_list

assert separate_into_words("look the dog ran fast") == ["look", "the", "dog", "ran", "fast"], 'Test Failed'
print('PASSED')

def reverse_word_order(string):
    original_list = separate_into_words(string)
    reversed_list = original_list[::-1]
    return str(reversed_list)

print(reverse_word_order("look the dog ran fast"))