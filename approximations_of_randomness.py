import math 
import sys
from monte_carlo_coin_flips import probability
from monte_carlo_coin_flips import monte_carlo_probability

# flips = {
#     Justin S =  ['HTTH', 'HHTT', 'TTHH', 'TTTH', 'HHTH', 'TTHT', 'HHHH', 'THHT', 'THTT', 'HTHH', 'TTTT', 'HTHT', 'TTHH', 'THTH', 'HTTH', 'HHTH', 'HHHT', 'TTTH', 'HTTH', 'HTHT']
#     'Nathan R': 'HTTH' 'HHTH' 'HTTT' 'HTHH' 'HTTH' 'HHHH' 'TTHH' 'TTHT' 'THTT' 'HTHT' 'HHTH' 'TTTT' 'THHT' 'HTTH' 'HTHH' 'THHH' 'HTTH' 'THTT' 'HHHT' 'HTHH'
#     'Justin H': 'HHHT HHTH HHTT THHT HTTT HTTT HHHT HTTT TTTT HTHT THHH TTHT TTHH HTHT TTTT HHHH THHH THTH HHHH THHT',
#     'Nathan A': 'HTTH HHHH THHH TTTH HTTT THTT HTHT THHT HTTH TTTT HHHH TTHH HHTH TTTH HHHH THTT HTHT TTTT HHTT HHTT',
#     'Cayden': 'HTHT HHTT HTTH THTH THHT TTHH HHHH TTTH HHHT HTTT TTHT HHTH HTHH THTT HHHH THTT HTTT HTHH TTTT HTTH',
#     'Maia': 'HTHH THTH HTTH TTTT TTHT HHHH HHTT THHH TTHH HHTH THHT HHHH THTT HHTH HTHT TTHH TTHH HHHH TTTT HHHT',
#     'Spencer': 'HHHT HTTH HTTT HTHH THTT TTHT TTTT HTTH HHTH TTHT TTHH HTHT THHT TTHT THTT THTH HTTH THHT TTTH HHHH',
#     'Charlie': 'HHHH HHHT HHTT HTTT TTTT TTTH TTHH THHH THTH HTHT HHTH HTHH TTHT THTT THTH TTHT HTHT THHT HTTH THTH',
#     'Anton': 'HHTH THTH TTTT HTTH THTT TTTH THHH TTHH THHT HHHH TTHT HTTT THTH HHHT HHTH HHHH TTTH HTHT TTTT HHTT',
#     'William': 'THTT HHHT HTTH THHT THTH HHHT TTTH HHTH THTH HTHT HHHT TTHT HHHT THTT HHTT TTHH HHTH TTTT THTH TTHT'
# }
flips = {
    'Justin S': 'HTTH HHTT TTHH TTTH HHTH TTHT HHHH THHT THTT HTHH TTTT HTHT TTHH THTH HTTH HHTH HHHT TTTH HTTH HTHT',
    'Nathan R': 'HTTH HHTH HTTT HTHH HTTH HHHH TTHH TTHT THTT HTHT HHTH TTTT THHT HTTH HTHH THHH HTTH THTT HHHT HTHH',
    'Justin H': 'HHHT HHTH HHTT THHT HTTT HTTT HHHT HTTT TTTT HTHT THHH TTHT TTHH HTHT TTTT HHHH THHH THTH HHHH THHT',
    'Nathan A': 'HTTH HHHH THHH TTTH HTTT THTT HTHT THHT HTTH TTTT HHHH TTHH HHTH TTTH HHHH THTT HTHT TTTT HHTT HHTT',
    'Cayden': 'HTHT HHTT HTTH THTH THHT TTHH HHHH TTTH HHHT HTTT TTHT HHTH HTHH THTT HHHH THTT HTTT HTHH TTTT HTTH',
    'Maia': 'HTHH THTH HTTH TTTT TTHT HHHH HHTT THHH TTHH HHTH THHT HHHH THTT HHTH HTHT TTHH TTHH HHHH TTTT HHHT',
    'Spencer': 'HHHT HTTH HTTT HTHH THTT TTHT TTTT HTTH HHTH TTHT TTHH HTHT THHT TTHT THTT THTH HTTH THHT TTTH HHHH',
    'Charlie': 'HHHH HHHT HHTT HTTT TTTT TTTH TTHH THHH THTH HTHT HHTH HTHH TTHT THTT THTH TTHT HTHT THHT HTTH THTH',
    'Anton': 'HHTH THTH TTTT HTTH THTT TTTH THHH TTHH THHT HHHH TTHT HTTT THTH HHHT HHTH HHHH TTTH HTHT TTTT HHTT',
    'William': 'THTT HHHT HTTH THHT THTH HHHT TTTH HHTH THTH HTHT HHHT TTHT HHHT THTT HHTT TTHH HHTH TTTT THTH TTHT'
}
def factorial_recursive(n):
    if n <= 1:
        return 1
    else:
        return n*factorial_recursive(n-1)

def count_heads(input_string):
    count = 0
    for char in input_string:
        if char == 'H':
            count += 1
    return count

def heads_distribution(input_string):
    flip_array = [0, 0, 0, 0, 0]
    lists = input_string.split(' ')
    for samples in lists:
        for num in range(5):
            if num == count_heads(samples):
                flip_array[num] += 1/20
    return flip_array

def true_distribution(num_heads, num_flips):
    outcome_num = 2**num_flips
    outcome_heads = factorial_recursive(num_flips)/((factorial_recursive(num_flips - num_heads))*factorial_recursive(num_heads))
    return outcome_heads/outcome_num

true_distribution_list = []

for num in range(5):
    true_distribution_list.append(true_distribution(num, 4))
print(true_distribution_list)

print(heads_distribution(flips['Spencer']))

def ln(x):
    return math.log(x)

def kl_divergence(p, q):
    result = 0
    for n in range(len(p)):
        if p[n] and q[n] != 0:
            result += p[n]*ln(p[n]/q[n])
    return round(result, 6)

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

sorted_tuple = []
for key in flips:
    sorted_tuple.append((key, kl_divergence(heads_distribution(flips[key]), true_distribution_list)))
print(sorted(sorted_tuple, key=lambda tup:(-tup[1], tup[0])))


#Charlie had the best approximation of a truly random flip. 
    

