

with open('rosalind_prot.txt') as stringfile:
    dna = ''.join(stringfile.read().split('\n'))

with open('codontable.txt') as stringfile:
    lib = stringfile.read().replace('\n', ' ').split()


output = open("output.txt", 'w')

for i in range(0, len(dna)-3, 3):
    for j in range(0, len(lib), 2):
        if dna[i:i+3] == lib[j]:
            output.write(lib[j+1])
            break

output.close()
