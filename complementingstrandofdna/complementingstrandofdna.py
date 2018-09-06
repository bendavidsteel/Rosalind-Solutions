
i = 0

with open('rosalind_revc.txt') as stringfile:
    s = [x.strip('\n') for x in stringfile.readlines()][0]

characters = list(s)
reverse = characters[::-1]
print(reverse)
for i in range(len(reverse)):
    if reverse[i] == "A":
        reverse[i] = "T"
    elif reverse[i] == "T":
        reverse[i] = "A"
    elif reverse[i] == "C":
        reverse[i] = "G"
    elif reverse[i] == "G":
        reverse[i] = "C"

s = ''.join(reverse)
    
output = open("output.txt", 'w')
output.write(s)
output.close()
