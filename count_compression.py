



def count_decompression(compressed_string):
    decompressed_string = ''

    for index in compressed_string: 
        for num in range(index[1]):
            decompressed_string += index[0] 
    return decompressed_string

assert count_decompression([('a',3), ('b',2), ('c',1), ('a',4)])
print('PASSED')

assert count_decompression([('2',2), ('3',1), ('4',5)])
print('PASSED')


def count_compression(string):
    compressed_list = []
    for index in range(len(string)):
        if string[index] == string[index - 1] and index != 0:
            compressed_list[-1][1] += 1 
        else:
            compressed_list.append([string[index], 1])
    for compressed_index in range(len(compressed_list)):
        compressed_list[compressed_index] = tuple(compressed_list[compressed_index])
    return compressed_list


assert count_compression('aaabbcaaaa') == [('a',3), ('b',2), ('c',1), ('a',4)], count_compression('aaabbcaaaa')
print('PASSED')

assert count_compression('22344444') == [('2',2), ('3',1), ('4',5)], 'test failed'
print('PASSED')