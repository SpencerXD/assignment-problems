def insert_element_into_sorted_list(element, sorted_list):
    for elements in range(len(sorted_list)):
        if element < sorted_list[elements]:
            sorted_list.insert(elements, element)
            return sorted_list
    sorted_list.append(element)
    return sorted_list

def card_sort(num_list):
    sorted_list = [num_list[0]]
    for element in range(1, len(num_list)):
        sorted_list = insert_element_into_sorted_list(num_list[element], sorted_list)
    return sorted_list

print('>>> card_sort([12, 11, 13, 5, 6])')
assert card_sort([12, 11, 13, 5, 6]) == [5, 6, 11, 12, 13], 'Test Failed'        
print('PASSED')

print('>>> card_sort([5, 7, 3, 5, 1, 3, -1, 1, -3, -1, -3, -1])')   
assert card_sort([5, 7, 3, 5, 1, 3, -1, 1, -3, -1, -3, -1]) == [-3, -3, -1, -1, -1, 1, 1, 3, 3, 5, 5, 7], 'Test Failed'
print('PASSED')