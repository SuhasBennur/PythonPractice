#Generate all permutations of a string
from itertools import permutations
s="abc"
print([''.join(p) for p in permutations(s)])
