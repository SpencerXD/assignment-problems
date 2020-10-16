import math 
import sys
from monte_carlo_coin_flips import probability
from monte_carlo_coin_flips import monte_carlo_probability

def ln(x):
    return math.log(x)

def kl_divergence(p, q):
    result = 0
    for n in range(len(p)):
        if p[n] and q[n] != 0:
            result += p[n]*ln(p[n]/q[n])
    return round(result, 6)
p = [0.2, 0.5, 0, 0.3]
q = [0.1, 0.8, 0.1, 0]
print(kl_divergence(p, q))

print('Computing KL Divergence for MC Simulations...')
print('100 samples --> KL Divergence =')
p = [monte_carlo_probability(n, 8, 100)for n in range(0, 8)]
q = [probability(n, 8) for n in range(0, 8)]
print(kl_divergence(p, q))

print('1000 samples --> KL Divergence =')
p = [monte_carlo_probability(n, 8, 1000)for n in range(0, 8)]
q = [probability(n, 8) for n in range(0, 8)]
print(kl_divergence(p, q))

print('10000 samples --> KL Divergence =')
p = [monte_carlo_probability(n, 8, 10000) for n in range(0, 8)]
q = [probability(n, 8) for n in range(0, 8)]
print(kl_divergence(p, q))


#As the number of samples increases, the KL divergence approaches 0. This is because as p approaches q, ln(p/q) goes to zero and D(p||q) = 0 

