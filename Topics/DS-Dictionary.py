#Dictionaries: key-value pair
d = {} #empty dictionary
print(type(d))
d1 = dict() #constructor call
print(type(d1))

d['sachin']=100
d['dhoni']=50
d['kholi']=25
print(d)
print('Score of Dhoni:',d['dhoni'])
d1 = {'sachin':100,'dhoni':98,'kholi':70,'dhoni':76}
#second value overrides first value here
print(d1)
d2 = {1:'Hi',2:'Hello',3:'Bye'}
d3 = {'one':'Hi','two':'Hello','three':'Bye'}
print(d2)
print(d3)
d4 = {'I':d1,'II':d2, 'III':d3}
for i in d4:
    print(i)
print('---')
for k,v in d4.items():
    print(k,v)
print('---')
d['rahul']=45
print(d)
if 'dhoni' in d:
    print('Yes, dhoni is there.')
else: 
    print('No, dhone is not there.')
print('list(d.keys()):',list(d.keys()))
print('list(d.values()):',list(d.values()))
print('list(d.items()):',list(d.items()))
print('d.items():',d.items())
ls1 = list(d.items())
print('ls1:',ls1,)
print('ls1[0:1]:',ls1[0:1])
print('ls1[1][0]:',ls1[1][0])
ls1.append(('jadesh',55))
d=dict(ls1) 
#list must contain values in tuple format 
# then only typecasting possible else no
print('d:',d)
print('Sorted d:',sorted(d))
#get of dictionary
dictEx = {'Tom':'Jerry', 'Power':'Rangers','Doraemon':'Nobita'}
print(dictEx.get('Shinchan','Not Found'))
print(dictEx.get('Doraemon','Found'))

# <class 'dict'>
# <class 'dict'>
# {'sachin': 100, 'dhoni': 50, 'kholi': 25}
# Score of Dhoni: 50
# {'sachin': 100, 'dhoni': 76, 'kholi': 70}
# {1: 'Hi', 2: 'Hello', 3: 'Bye'}
# {'one': 'Hi', 'two': 'Hello', 'three': 'Bye'}
# I
# II
# III
# ---
# I {'sachin': 100, 'dhoni': 76, 'kholi': 70}
# II {1: 'Hi', 2: 'Hello', 3: 'Bye'}
# III {'one': 'Hi', 'two': 'Hello', 'three': 'Bye'}
# ---
# {'sachin': 100, 'dhoni': 50, 'kholi': 25, 'rahul': 45}
# Yes, dhoni is there.
# list(d.keys()): ['sachin', 'dhoni', 'kholi', 'rahul']
# list(d.values()): [100, 50, 25, 45]
# list(d.items()): [('sachin', 100), ('dhoni', 50), ('kholi', 25), ('rahul', 45)]
# d.items(): dict_items([('sachin', 100), ('dhoni', 50), ('kholi', 25), ('rahul', 45)])
# ls1: [('sachin', 100), ('dhoni', 50), ('kholi', 25), ('rahul', 45)]
# ls1[0:1]: [('sachin', 100)]
# ls1[1][0]: dhoni
# d: {'sachin': 100, 'dhoni': 50, 'kholi': 25, 'rahul': 45, 'jadesh': 55}
# Sorted d: ['dhoni', 'jadesh', 'kholi', 'rahul', 'sachin']
# Not Found
# Nobita