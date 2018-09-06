a = 0
c = 0
g = 0
t = 0
i = 0


with open('rosalind_dna.txt') as stringfile:
    s = [x.strip('\n') for x in stringfile.readlines()][0]

for i in range(len(s)):
    if s[i] == 'A':
        a += 1
    elif s[i] == 'C':
        c += 1
    elif s[i] == 'G':
        g += 1
    elif s[i] == 'T':
        t += 1
    
output = open("output.txt", 'w')
output.write(str(a) + ' ' + str(c) + ' ' + str(g) + ' ' + str(t))
output.close()
