#string function

for i in ('Hello'):
    print(i)

# H
# e
# l
# l
# o

#sum of digits in a given no if no is string
no=input('Enter no:')
print('Entered no is:',no)
sum=0
for i in no:
        print(sum,'+',int(i),'=',sum + int(i))
        sum = sum + int(i)
print('Total sum is:',sum)
print('------------')
sum_digit=0
num=int(no)
while (num>0):
        rem = num % 10
        sum_digit = sum_digit + rem
        num = num//10
print('Total sum by modulus way is:',sum_digit)

# Entered no is: 23
# 0 + 2 = 2
# 2 + 3 = 5
# Total sum is: 5
# ------------
# Total sum by modulus way is: 5