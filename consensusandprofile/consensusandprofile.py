
with open('rosalind_cons.txt') as stringfile:
    data = [list(x)[13:] for x in stringfile.read().replace('\n', '').split('>')[1:]]

mat = []
print(data)

lets = {0:"A", 1:"C", 2:"G", 3:"T"}

for i in range(len(data[0])):
    mat.append([])
    mat[i] = [0,0,0,0]
    for j in range(len(data)):
        if data[j][i] == "A":
            mat[i][0] += 1
        elif data[j][i] == "C":
            mat[i][1] += 1
        elif data[j][i] == "G":
            mat[i][2] += 1
        elif data[j][i] == "T":
            mat[i][3] += 1


output = open("output.txt", 'w')


for dat in mat:
    output.write(lets[dat.index(max(dat))])

output.write('\n')

output.write("A:")
for dat in mat:
    output.write(" " + str(dat[0]))
output.write('\n')

output.write("C:")
for dat in mat:
    output.write(" " + str(dat[1]))
output.write('\n')

output.write("G:")
for dat in mat:
    output.write(" " + str(dat[2]))
output.write('\n')

output.write("T:")
for dat in mat:
    output.write(" " + str(dat[3]))
output.write('\n')

output.close()

