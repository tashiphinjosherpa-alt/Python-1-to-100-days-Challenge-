
# Default parameter
def calculate_Area(l, b=23):
    A = l * b
    return A

l = 12
b = 23

print(f'Area is {calculate_Area(l, b=2)}')
print(f'Area is {calculate_Area(l)}')
