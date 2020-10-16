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

def monte_carlo_probability(num_heads, num_flips, iterations):
    samples = []
    num_samples_with_exactly_num_heads = 0
    for i in range(iterations):
        sample = [random_coin_flip() for _ in range(num_flips)]
        samples.append(sample)
    num_samples_with_exactly_1_head = 0
    for sample in samples:
        num_heads_in_sample = 0
        for flip_result in sample:
            if flip_result == 'H':
                num_heads_in_sample +=1
        if num_heads_in_sample == num_heads:
            num_samples_with_exactly_num_heads += 1
    return num_samples_with_exactly_num_heads/iterations

assert probability(5,8) == 0.21875, 'test failed'
if __name__ == "__main__":
    print('PASSED')


if __name__ == "__main__":
    print(probability(4,6))

    print(monte_carlo_probability(0,0, 1000))
    print(monte_carlo_probability(5,8, 1000))
    print(monte_carlo_probability(5,8, 1000))
    print(monte_carlo_probability(5,8, 1000))
    print(monte_carlo_probability(5,8, 1000))
