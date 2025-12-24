# looping structure (while, for)
print('--While Loop--')
i=0
while i<5:
    print(i)
    i=i+1
n=int(input('Enter a number:'))
print('--For loop with range (0,',n,')--')
for i in range(0,n):
    print(i)
print('--For loop with positve range (0,',n,',3)--')
for i in range(0,n,3):
    print(i)
print('--For loop with negative range (',n,',0,-2)--')
for i in range(n,0,-2):
    print(i)

# --While Loop--
# 0
# 1
# 2
# 3
# 4
# --For loop with range (0, 5 )--
# 0
# 1
# 2
# 3
# 4
# --For loop with positve range (0, 5 ,3)--
# 0
# 3
# --For loop with negative range ( 5 ,0,-2)--
# 5
# 3
# 1


    #loop break & continue
for i in range(6):
    if i==4:
        break
    print(i)
print('breaks once i=4')
print('---')
for i in range(6):
    if i==4:
        continue
    print(i)
print('skips 4 and continue')

# 0
# 1
# 2
# 3
# breaks once i=4
# ---
# 0
# 1
# 2
# 3
# 5
# skips 4 and continue