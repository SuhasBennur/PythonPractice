#List (mutable)
listEx=[10,'s',10.5,4,6,'t','Guess',[1,2,5,4]]
print('listEx:',listEx)
print('listEx[1]:',listEx[1])
print('listEx[0:2]:',listEx[0:2])
print('listEx[::-1]:',listEx[::-1])
print('listEx[6][1:3]:',listEx[6][1:3])
print('listEx[:-1]:',listEx[-1][2])
print('----')
lst=[2,6,7]
lst1=[4,'a']
lst.append(5)
print('lst.append(5):',lst)
lst.append('s')
print('lst.append(''s''):',lst)
lst1.extend(lst)
print('lst1.extend(lst):',lst1)
print('lst:',lst)
lst.pop(1)
print('lst.pop(1)/remove at index:',lst)
lst.remove(2)
print('lst.remove(2)/remove element itself:',lst)
lst.reverse()
print('lst.reverse():',lst)
lst.pop(0)
lst.sort()
print('lst.sort() in ascending:',lst)
lst.sort(reverse=True)
print('lst.sort(reverse=True) in descending:',lst)
lst.insert(1,10)
print('lst.insert(1,10):',lst)
print('lst1:',lst1)
del lst1[3]
print('del lst1[3]:',lst1)
del lst1[0:4:2]
print('del lst1[0:4:2]',lst1)
lst1.clear()
print('after lst1.clear():',lst1)

# listEx: [10, 's', 10.5, 4, 6, 't', 'Guess', [1, 2, 5, 4]]
# listEx[1]: s
# listEx[0:2]: [10, 's']
# listEx[::-1]: [[1, 2, 5, 4], 'Guess', 't', 6, 4, 10.5, 's', 10]
# listEx[6][1:3]: ue
# listEx[:-1]: 5
# ----
# lst.append(5): [2, 6, 7, 5]
# lst.append(s): [2, 6, 7, 5, 's']
# lst1.extend(lst): [4, 'a', 2, 6, 7, 5, 's']
# lst: [2, 6, 7, 5, 's']
# lst.pop(1)/remove at index: [2, 7, 5, 's']
# lst.remove(2)/remove element itself: [7, 5, 's']
# lst.reverse(): ['s', 5, 7]
# lst.sort() in ascending: [5, 7]
# lst.sort(reverse=True) in descending: [7, 5]
# lst.insert(1,10): [7, 10, 5]
# lst1: [4, 'a', 2, 6, 7, 5, 's']
# del lst1[3]: [4, 'a', 2, 7, 5, 's']
# del lst1[0:4:2] ['a', 7, 5, 's']
# after lst1.clear(): []

#split is a string method but returns a list
#join is string method which accept list as argument

strEx = 'This is just an example'
print('strEx:',strEx)
lstEx=strEx.split()
print('strEx.split():',lstEx)
strDt = '23-05-2025'
print('strDt:',strDt)
print('strDt.split():',strDt.split('-'))

delmt='/'
strdts = delmt.join(strDt)
print('delmt.join(strDt):',strDt)
print('lstEx:','_'.join(lstEx))
print('lstEx:',' '.join(lstEx))

# strEx: This is just an example
# strEx.split(): ['This', 'is', 'just', 'an', 'example']
# strDt: 23-05-2025
# strDt.split(): ['23', '05', '2025']
# delmt.join(strDt): 23-05-2025
# lstEx: This_is_just_an_example
# lstEx: This is just an example

#here lst2 referencing lst1, 
# so if we modify lst2, lst1 
# is also get modify

lst1=[10,20,30,40]
lst2=lst1
lst2[2]=50
print('lst1',lst1)
print('lst2',lst2)
print('id(lst1)',id(lst1))
print('id(lst2)',id(lst2))
print('--------')
#here lst4 is copying elements of lst4, 
# hence data is not modifying in lst3 
# if we change something in lst4

lst3=[50,60,70,80]
lst4=lst3.copy() #shallocopy
lst4[2]=90
print('lst3',lst3)
print('lst4',lst4)
print('id(lst3)',id(lst3))
print('id(lst4)',id(lst4))
print('--------')
#Here inner list is also get modifies even 
# if we apply copy because copy is copying 
# address of inner list from outerlist rather 
# than elements which is why it is referencing

lst5=[1,2,[10,20],3,4]
print('lst5:',lst5)
lst6=lst5.copy() #shallocopy
print('lst6:',lst6)
lst6[2][1]=30
lst6[3]=5
print('lst6:',lst6)
print('lst5:',lst5)
print('id(lst6[2])',id(lst6[2]))
print('id(lst5[2])',id(lst5[2]))
print('--------')

# to avoid this we use deepcopy from copy
import copy

lst7=[11,22,[101,201],33,44]
print('lst7:',lst7)
lst8=copy.deepcopy(lst7)
print('lst8:',lst8)
lst8[2][1]=303
lst8[3]=55
print('lst8:',lst8)
print('lst7:',lst7)
print('id(lst8[2])',id(lst8[2]))
print('id(lst7[2])',id(lst7[2]))

# lst1 [10, 20, 50, 40]
# lst2 [10, 20, 50, 40]
# id(lst1) 2806890863296
# id(lst2) 2806890863296
# --------
# lst3 [50, 60, 70, 80]
# lst4 [50, 60, 90, 80]
# id(lst3) 2806890844608
# id(lst4) 2806890863616
# --------
# lst5: [1, 2, [10, 20], 3, 4]
# lst6: [1, 2, [10, 20], 3, 4]
# lst6: [1, 2, [10, 30], 5, 4]
# lst5: [1, 2, [10, 30], 3, 4]
# id(lst6[2]) 2806890863168
# id(lst5[2]) 2806890863168
# --------
# lst7: [11, 22, [101, 201], 33, 44]
# lst8: [11, 22, [101, 201], 33, 44]
# lst8: [11, 22, [101, 303], 55, 44]
# lst7: [11, 22, [101, 201], 33, 44]
# id(lst8[2]) 2806890861824
# id(lst7[2]) 2806890862912