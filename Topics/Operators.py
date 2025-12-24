# Arithematic operators
x=10
xa=3
y=10.5
z=True
xy=x+y
print('Sum of x & y is ', xy, type(xy))
xy=x-y
print('Difference of x & y is ', xy, type(xy))
xy=x*y
print('Multiplication of x & y is ', xy, type(xy))
xy=x/xa
print('Division of x & xa is ', xy, type(xy))
xy=x//xa
print('Integer Division of x & xa is ', xy, type(xy))
xy=x%xa
print('Modulus of x & xa is ', xy, type(xy))
xy=x**2
print('Power of x to 2 is ',xy, type(xy))


# Sum of x & y is  20.5 <class 'float'>
# Difference of x & y is  -0.5 <class 'float'>
# Multiplication of x & y is  105.0 <class 'float'>
# Division of x & xa is  3.3333333333333335 <class 'float'>
# Integer Division of x & xa is  3 <class 'int'>
# Modulus of x & xa is  1 <class 'int'>
# Power of x to 2 is  100 <class 'int'>

# Logical operators
n1 = 12
n2 = 40
print('Is',n1,'greater than',n2,'?', n1>n2)
print('Is',n1,'smaller than',n2,'?', n1<n2)
print('Is',n1,'equals to',n2,'?', n1==n2)
print('Is',n1,'not equals to',n2,'?', n1!=n2)

n = (n1>5) or (n2>30)
print(n)
n = (n1==5) and (n2>30)
print(n)
print(not n)

# Is 12 greater than 40 ? False
# Is 12 smaller than 40 ? True
# Is 12 equals to 40 ? False
# Is 12 not equals to 40 ? True
# True
# False
# True