from random import random

def factorial_recursive(n):
    if n <= 1:
        return 1
    else:
        return n*factorial_recursive(n-1)

def probability(num_heads, num_flips):
    outcome_num = 2**num_flips
    outcome_heads = factorial_recursive(num_flips)/((factorial_recursive(num_flips - num_heads))*factorial_recursive(num_heads))
    return outcome_heads/outcome_num

def random_coin_flip():
    index = round(random())
    return 'TH'[index]



def monte_carlo_probability(num_heads, num_flips):
    samples = []

    for i in range(1000):
        sample = [random_coin_flip() for _ in range(3)]
        samples.append(sample)

    num_samples_with_exactly_1_head = 0
    for sample in samples:
        num_heads_in_sample = 0
        for flip_result in sample:
            if flip_result == 'H':
                num_heads_in_sample +=1
        if num_heads_in_sample == 1:
            num_samples_with_exactly_1_head += 1
    return num_samples_with_exactly_1_head/1000

assert probability(5,8) == 0.21875, 'test failed'
print('PASSED')

print(probability(5,8))

print(monte_carlo_probability(5,8))
