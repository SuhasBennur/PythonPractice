# User Input and output
x = input('Enter one number:')
print('You have entered:',x, type(x))
x1 = int(input('Enter one integer number:'))
print('You have entered:',x1, type(x1))
x2 = float(input('Enter one floating number:'))
print('You have entered:',x2, type(x2))
y = input('Enter your name:')
print('Your name is:', y, type(y))

# You have entered: 23 <class 'str'>
# You have entered: 43 <class 'int'>
# You have entered: 23.4 <class 'float'>
# Your name is: suhas <class 'str'>

# Area of circle
import math

r = float(input('Enter radius:'))
area = math.pi * r**2
print('Area of Circle for the redius',r,'is:', area)

# Area of Circle for the redius 24.0 is: 1809.5573684677208

# Area of triangle
b = int(input('Enter triangle base:'))
h = int(input('Enter triangle height:'))
area = b * h * 0.5
print('Area of triangle for base',b,'and height',h ,'is:',area)

#Area of triangle for base 24 and height 12 is: 144.0