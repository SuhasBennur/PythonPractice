# control Structure
# conditional structure (if,if-else, if-elif) 


marks = float(input('Enter marks of student:'))
print('Student marks is:'+str(marks))
if marks>35:
    print('Student is pass')
else:
    print('Student is fail')

if marks>35 and marks < 50:
    print('Student is passed in Third class')
else:
    if marks<35:
        print('Student is fail')

if marks>50 and marks<60:
    print('Student passeed in Second class')
elif marks>60 and marks<85:
    print('Student passed in First class')
elif marks>85:
    print('Student passed in distinction.')
else:
    print('Exception')

# Student marks is:35.0
# Student is fail
# Exception