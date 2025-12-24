# user defined function
def printstmt():
    print('This is inner function')

def outerfunction():
    print('This is outer function')
    printstmt()

outerfunction()

# This is outer function
# This is inner function

def addition(a,b):
    return a + b

print('Addition of numbers:',addition(5,6))
print('Addition of characters:',addition('H','i'))
c1 = 'Hello '
c2 = 'World'
print('Addition of Strings')
addition(c1, c2)

# Addition of numbers: 11
# Addition of characters: Hi
# Addition of Strings
# 'Hello World'