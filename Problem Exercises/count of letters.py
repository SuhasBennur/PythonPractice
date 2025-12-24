s = 'Hello how are you?'
d = {}
for i in s:
    if i in d.keys():
        d[i]=d[i]+1
    else:
        d[i]=1
print('d1:',list(d.items()))

# d1: [('H', 1), ('e', 2), ('l', 2), ('o', 3), (' ', 3), ('h', 1), ('w', 1), ('a', 1), ('r', 1), ('y', 1), ('u', 1), ('?', 1)]

print('----------------------------------------------------------------------')
# another way
d1 = {}
for i in s:
    d1[i] = s.count(i)
print('d2:',list(d1.items()))

# d2: [('H', 1), ('e', 2), ('l', 2), ('o', 3), (' ', 3), ('h', 1), ('w', 1), ('a', 1), ('r', 1), ('y', 1), ('u', 1), ('?', 1)]

print('----------------------------------------------------------------------')
#another way
inp = 'Hi Hello how are you uu'
output = {}
for i in inp:
    if i in output:
        output[i] +=1
    else:
        output[i] = 1
print(output)

# {'H': 2, 'i': 1, ' ': 5, 'e': 2, 'l': 2, 'o': 3, 'h': 1, 'w': 1, 'a': 1, 'r': 1, 'y': 1, 'u': 3}

print('----------------------------------------------------------------------')
# another way - most efficient way
d3 = {}
for i in s:
    d3[i] = d3.get(i,0)+1
print('d3:',list(d3.items()))

# d3: [('H', 1), ('e', 2), ('l', 2), ('o', 3), (' ', 3), ('h', 1), ('w', 1), ('a', 1), ('r', 1), ('y', 1), ('u', 1), ('?', 1)]

print('----------------------------------------------------------------------')
# count of words
s1 = 'Hello, How are you How about you'
d3={}
for i in s1.split(' '):
    d3[i] = d3.get(i,0)+1
print('d3:',list(d3.items()))

# d3: [('Hello,', 1), ('How', 2), ('are', 1), ('you', 2), ('about', 1)]