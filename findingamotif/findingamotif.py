
with open('rosalind_subs.txt') as stringfile:
    data = stringfile.read().split('\n')

s = data[0]
t = data[1]

output = open("output.txt", 'w')

for i in range(len(s)):
    if t == s[i:i+len(t)]:
        output.write(str(i+1) + ' ')


output.close()
