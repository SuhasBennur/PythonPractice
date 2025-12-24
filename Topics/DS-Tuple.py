#tuple - immutable

t1 = (1,2,3,4,'Sam')
t2 = 11,12,13,14,'ram'
print(t1)
print(t2)
print(t1[2])

x,y = 10,20
print('x:',x,'y:',y)
x,y = y,x
print('x:',x,'y:',y)
print('----')
#tuple to list -> list to tuple
print(t1,type(t1))
l1 = list(t1)
print(l1,type(l1))
l1 = [1,2,3,4]
t1 = tuple(l1)
print(t1,type(t1))
#string to tuple
str1 = "Python"
t3 = tuple(str1)
print(t3)

# (1, 2, 3, 4, 'Sam')
# (11, 12, 13, 14, 'ram')
# 3
# x: 10 y: 20
# x: 20 y: 10
# ----
# (1, 2, 3, 4, 'Sam') <class 'tuple'>
# [1, 2, 3, 4, 'Sam'] <class 'list'>
# (1, 2, 3, 4) <class 'tuple'>
# ('P', 'y', 't', 'h', 'o', 'n')