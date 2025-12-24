#Sets : used to convert unordered, unidexed and 
# collection of elements into ordered elements 
# without any duplications
# single element within flower bracket is set, 
# where as key value pair within parenthesis is dict
# duplicates removed while adding itself
s = set()
s = {'apple','banana','Grapes'}
s = {'apple','banana','Grapes', 'apple'}
print(s)

listEx = [1,5,6,12,76,12,5,2,6,1,12]
setEx=set(listEx)
print(setEx)
listEx2 = list(setEx)
print(listEx2)
#in one line
listEx3 = list(set([12,54,12,5,4,3,5,3,12,45]))
print(listEx3)

# {'apple', 'banana', 'Grapes'}
# {1, 2, 5, 6, 12, 76}
# [1, 2, 5, 6, 12, 76]
# [3, 4, 5, 12, 45, 54]