


with open('rosalind_dna.txt') as stringfile:
    s = [x.strip('\n') for x in stringfile.readlines()][0]

characters = list(s)
reverse = characters[::-1]
for i in reverse:
    if i == "A":
        i = "T"
    elif i == "T":
        i = "A"
    elif i == "C":
        i = "G"
    elif i == "G":
        i = "C"

s = ''.join(characters)
    
output = open("output.txt", 'w')
output.write(s)
output.close()
