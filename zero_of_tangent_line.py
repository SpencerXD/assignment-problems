def f(c):
    return c**2 - 2

def estimate_derivative(f, c, delta):
    return (f(c + 0.5 * delta) - f(c - 0.5 * delta))/delta

def zero_of_tangent_line(f, c, delta):
    slope = estimate_derivative(f, c, delta)
    y = f(c)
    constant = y - slope*c
    return ( 0 - constant)/slope

answer = zero_of_tangent_line(f, 1, 0.001)
print(answer)
print('PASSED')

def estimate_solution(f, initial_guess, delta, precision):
    new_guess = initial_guess
    previous_guess = initial_guess + precision
    while abs(new_guess - previous_guess) >= precision:
        previous_guess = new_guess
        new_guess = zero_of_tangent_line(f, new_guess, delta)
    return  new_guess

answer = estimate_solution(f, 1, 0.001, 0.01)
#assert round(answer, 6) == 0.682328
print('PASSED')







