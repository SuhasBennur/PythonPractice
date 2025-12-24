#DataStructure (strings, lists, tuples, dictionaries,set)
#string (Immutable)
# ASCII Values: 
# A-Z: 65-91,
# a-z: 97-122,
# 0-9: 48-57,
# white space: 32,
# enter key: 13 #
print('ASCII of A:',ord('A'))
strexample='Abracadabra'
print('Word:',strexample)
for i in range(0,strexample.__len__()):
    print(i,end=' ')
print('')
for i in range(0,strexample.__len__()):
    print(strexample[i], end=' ')
print('')
print('[start:End:Stride]')
print('strexample[0:]:',strexample[0:])
print('strexample[0]:',strexample[0])
print('strexample[::-1]:',strexample[::-1])
print('strexample[5:7]:',strexample[5:7])
print('strexample[:7]:',strexample[:7])
print('strexample[-1]:',strexample[-1])
print('strexample[:-1]:',strexample[:-1])
print('strexample[9:-1]:',strexample[9:-1])
print('strexample[0:10:2]:',strexample[0:10:2])
print('strexample[0:10:3]:',strexample[0:10:3])
print('strexample[8:2:-2]:',strexample[8:2:-2])
print('------')
print('strexample.count(''a''):',strexample.count('a'))
print('strexample.count(''A''):',strexample.count('A'))
print('strexample.count(''ra''):',strexample.count('ra'))
print('strexample.__len__():',strexample.__len__())
print('strexample.find(''cad''):',strexample.find('cad'))
print('strexample.find(''br'',6,10):',strexample.find('br',6,10))
print('strexample.upper():',strexample.upper())
print('strexample.lower():',strexample.lower())
strexample1=strexample.replace('Abra','Cbra')
print('strexample1:',strexample1)
print('strexample.replace(''Abra'',''Cbra'')',strexample1)
print('strexample.strip(''a'')',strexample1.strip('a'))

scrapdata='$56@^Perfect%@'
print('scrapdata:',scrapdata)
print('Pure data:',scrapdata.strip('$@%^56'))

# ASCII of A: 65
# Word: Abracadabra
# 0 1 2 3 4 5 6 7 8 9 10 
# A b r a c a d a b r a 
# [start:End:Stride]
# strexample[0:]: Abracadabra
# strexample[0]: A
# strexample[::-1]: arbadacarbA
# strexample[5:7]: ad
# strexample[:7]: Abracad
# strexample[-1]: a
# strexample[:-1]: Abracadabr
# strexample[9:-1]: r
# strexample[0:10:2]: Arcdb
# strexample[0:10:3]: Aadr
# strexample[8:2:-2]: bdc
# ------
# strexample.count(a): 4
# strexample.count(A): 1
# strexample.count(ra): 2
# strexample.__len__(): 11
# strexample.find(cad): 4
# strexample.find(br,6,10): 8
# strexample.upper(): ABRACADABRA
# strexample.lower(): abracadabra
# strexample1: Cbracadabra
# strexample.replace(Abra,Cbra) Cbracadabra
# strexample.strip(a) Cbracadabr

# scrapdata: $56@^Perfect%@
# Pure data: Perfect