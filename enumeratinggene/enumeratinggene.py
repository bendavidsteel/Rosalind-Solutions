import math
import itertools

with open('rosalind_perm.txt') as stringfile:
    data = ''.join(stringfile.read().split('\n'))

n = int(data)
ns = []

output = open("output.txt", 'w')
output.write(str(math.factorial(n)) + '\n')

for i in range(1, n+1):
    ns.append(i)

for p in itertools.permutations(ns):
    for num in p:
        output.write(str(num) + ' ')
    output.write('\n')
    

output.close()





