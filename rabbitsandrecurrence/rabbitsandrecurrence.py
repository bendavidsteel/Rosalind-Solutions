

with open('rosalind_fib.txt') as stringfile:
    s = stringfile.read().split()

print(s)

n = int(s[0])
k = int(s[1])

f1 = 1
f2 = 1

m2 = f1
m1 = f2

for i in range(n-2):
    fn = m1+(k*m2)
    m2 = m1
    m1 = fn

output = open("output.txt", 'w')
output.write(str(fn))
output.close()
