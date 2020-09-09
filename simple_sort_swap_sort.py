def simple_sort(num_list):
    final_list = []
    for inputs in range(len(num_list)):
        minimum = num_list[0]
        for num in num_list:
            if num < minimum:
                minimum = num
        final_list.append(minimum)
        num_list.remove(minimum)
    return final_list

print('>>> simple_sort([5,8,2,2,4,3,0,2,-5,3.14,2])')
assert simple_sort([5,8,2,2,4,3,0,2,-5,3.14,2]) == [-5,0,2,2,2,2,3,3.14,4,5,8], 'Test Failed'
print('PASSED')


def swap_sort(x):
    for inputs in range(len(x)):
        for num in range(len(x)-1):
            if x[num+1] < x[num]:
                x[num+1], x[num] = x[num], x[num+1]
    return x

print('>>> swap_sort([5,8,2,2,4,3,0,2,-5,3.14,2])')
assert swap_sort([5,8,2,2,4,3,0,2,-5,3.14,2]) == [-5,0,2,2,2,2,3,3.14,4,5,8], 'Test Failed'
print('PASSED')
