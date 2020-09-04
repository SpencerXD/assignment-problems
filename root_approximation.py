def update_bounds(bounds):
    if ((bounds[1] + bounds[0])/2)**2 < 2:
        bounds[0] = ((bounds[1] + bounds[0])/2)
    else:
        bounds[1] = ((bounds[1] + bounds[0])/2)
    return bounds
print('>>> update_bounds([1, 2])')
assert update_bounds([1, 2]) == [1, 1.5], 'Test Failed'
print('PASSED')

print('>>> update_bounds([1, 1.5])')
assert update_bounds([1, 1.5]) == [1.25, 1.5], 'Test Failed'
print('PASSED')

def estimate_root(precision):
    new_bounds = update_bounds([1, 2])
    while new_bounds[1] - new_bounds[0] > 0.1:
        new_bounds = update_bounds(new_bounds)
    return (new_bounds[1] + new_bounds[0])/2

print(">>> estimate_root(0.1)")
assert estimate_root(0.1) == 1.40625, "Test Failed"
print('PASSED')