import matplotlib.pyplot as plt

def collatz_iterations(number):
    iterations = 0
    while number != 1:
        if number%2 == 0:
            number = number/2
            iterations += 1
        else:
            iterations += 1
            number = 3*number + 1 
    return iterations

print('>>> collatz_iterations(13)')
assert collatz_iterations(13) == 9, 'Test Failed'
print('PASSED')


current_greatest = 0
for number in range(1, 1001):
    collatz_iterations(number)
    if collatz_iterations(number) > current_greatest:
        current_greatest = collatz_iterations(number)
        current_greater_num = number

print(current_greater_num)


plt.style.use('bmh')
x_coords = [x for x in range(1, 1001)]
y_coords = [collatz_iterations(x) for x in range(1, 1001)]
plt.plot(x_coords, y_coords)
plt.xlabel('X-Axis Label')
plt.ylabel('Y-Axis Label')
plt.title('This is the title of the plot!')
plt.savefig('plot.png')