# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools
s,n = list(map(str,input().split(' ')))
s = sorted(s)
for p in list(itertools.permutations(s,int(n))):
    print(''.join(p))
