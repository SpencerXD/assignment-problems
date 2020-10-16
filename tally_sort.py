def tally_sort(num_list):
    minimum = num_list[0]
    tally_array = [0 for n in range(len(num_list))]
    new_list = []
    sorted_array = []

    for num in num_list:
        if num < minimum:
            minimum = num 

    for num in num_list:   
        new_list.append(num-minimum)

    for num in num_list:
        tally_array[num] +=1 

    for index in range(len(tally_array)):
        for i in range(tally_array[index]):
            sorted_array.append(index + minimum)

    return sorted_array


print('>>> tally_sort([2, 5, 2, 3, 8, 6, 3])')
assert tally_sort([2, 5, 2, 3, 8, 6, 3]) == [2, 2, 3, 3, 5, 6, 8], 'Test Failed'
print('PASSED')

print(tally_sort([2, 5, 2, 3, 8, 6, 3]))