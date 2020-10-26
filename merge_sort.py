def merge(x,y):
    sorted_list = []
    length = range(len(x) + len(y))
    for a in length:
        if len(x) > 0:
            minimum_x = min(x) 
        else:
            minimum_x = 100000
        if len(y) > 0:
            minimum_y = min(y)
        else:
            minimum_y = 100000
        if minimum_x < minimum_y:
            minimum = minimum_x
        else: 
            minimum = minimum_y
        if minimum == minimum_x:
            current_list = x
        else: 
            current_list = y
        sorted_list.append(minimum)
        del current_list[current_list.index(minimum)]
    return sorted_list



assert merge([-2,1,4,4,4,5,7],[-1,6,6]) == [-2,-1,1,4,4,4,5,6,6,7]
print('PASSED')

def merge_sort(input_list):
    if len(input_list) > 1:
        middle_index = int(len(input_list)/2)
        left = input_list[:middle_index]
        right = input_list[middle_index:]
        left = merge_sort(left)
        right = merge_sort(right)
        return merge(left, right)
    else:
        return input_list

assert merge_sort([4,8,7,7,4,2,3,1]) == [1,2,3,4,4,7,7,8]
print('PASSED')
