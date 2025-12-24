#Dictionary Comprehensions
# {key_expression: value_expression for item in iterable if condition}

kp = {x: x+10 for x in range(10)}
print('KP:',kp)

squares = {x: x**2 for x in range(5)}
print('squares:',squares,'\n')

even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print('even_squares:',even_squares,'\n')

def cube(n): return n**3
cubes = {x: cube(x) for x in range(1, 6)}
print('cubes:',cubes,'\n')

original = {'a': 1, 'b': 2, 'c': 3}
swapped = {v: k for k, v in original.items()}
print('swapped:',swapped,'\n')

