def factorial_recursive(n):
    if n <= 1:
        return 1
    else:
        return n*factorial_recursive(n-1)


num_possibilities = 2**5
num_heads = factorial_recursive(5)/((factorial_recursive(5 - 2))*factorial_recursive(2))
probability = num_heads/num_possibilities
print(probability)

numbers_ending_1 = [n  for n in range(1, 1001) if n % 10 == 2]

print(numbers_ending_1)