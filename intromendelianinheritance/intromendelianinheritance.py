import math


kkprob = 1
kmprob = 1
knprob = 1
mmprob = 0.75
mnprob = 0.5
nnprob = 0

with open('rosalind_iprb.txt') as stringfile:
    s = [x.strip('\n') for x in stringfile.readlines()][0]

sample = s.split(' ')
k = int(sample[0])
m = int(sample[1])
n = int(sample[2])


tot = ((k+m+n)*(k+m+n-1))**-1

kktot = k*(k-1)*tot
kmtot = k*m*tot
kntot = k*n*tot
mmtot = m*(m-1)*tot
mntot = m*n*tot
nntot = n*(n-1)*tot

nowithdom = (kkprob*kktot)+(2*kmprob*kmtot)+(2*knprob*kntot)+(mmprob*mmtot)+(2*mnprob*mntot)+(nnprob*nntot)

print(nowithdom)
    
output = open("output.txt", 'w')
output.write(str(nowithdom))
output.close()
