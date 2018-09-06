import math

maxcontent = 0


with open('rosalind_gc.txt') as stringfile:
    s = stringfile.read().replace('\n', '').split('>')
    del s[0]


print(s)

for i in range(len(s)):
    index = s[i][0:13]
    content = 0
    for n in range(13, len(s[i])):
        if s[i][n] == 'C':
            content += 1
        elif s[i][n] == 'G':
            content += 1
    print(content)
    print(len(s[i])-13)
    if (content/(len(s[i])-13)) > maxcontent:
        maxcontent = content/(len(s[i])-13)
        
        maxindex = index

output = open("output.txt", 'w')
output.write(maxindex + '\n')
output.write(str(maxcontent*100))
output.close()
