import math 

def estimate_derivative(f, c, delta):
    return (f(c + 0.5 * delta) - f(c - 0.5 * delta))/delta

def f(c):
    return c**2+2*c+1

def h(c):
    return (c**2 + math.cos(c))/(math.e**math.sin(c))

def gradient_descent(f,x0,alpha=0.01,delta=0.0001,iterations=10000):
    for iteration in range(iterations):
        x0 = x0 - alpha * estimate_derivative(f, x0, delta)
    return f(x0)

print(gradient_descent(f, 0))

print(gradient_descent(h, 0))