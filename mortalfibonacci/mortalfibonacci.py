

with open('sample.txt') as stringfile:
    s = stringfile.read().split()


n = int(s[0])
k = int(s[1])

pop = [0, 1, 1]

for i in range(3, n+1):
    pop.append(pop[-1]+(pop[-2]*2))
    if i >= k:
        pop[-1] -= pop[-k]-pop[-k-1]
    

print(pop)

output = open("output.txt", 'w')
output.write(str(pop[-1]))
output.close()
