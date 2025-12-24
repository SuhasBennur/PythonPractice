#List Comprehension(LSCH)
# using list cmph, we will be able to combine 
# mulitple tasks on lists with 
# loops and ctrl structures


#instead of this
ls1 = [1,2,3,4,5]
print('List 1:',ls1)
#usual way
ls2=[]
for i in range(1,6):
    ls2.append(i)
print('List 2:',ls2)
#using LSCH
ls3=[i for i in range(1,6)]
print('List 3:',ls3)
#even no list
ls4=[i for i in range(1,12) if i%2==0]
print('List 4:',ls4)

#usual way
lstLength = int(input('Enter total no elements in a list:'))
listt=[]
for i in range(0,lstLength):
    lstE = int(input('Enter list elements'))
    listt.append(lstE)
print('List:',listt)

#with LSCH
n = int(input('Enter n:'))
listt1=[int(input('Enter element:')) for i in range(n)]
print('List:',listt1)

