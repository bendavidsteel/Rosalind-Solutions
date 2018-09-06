
with open('rosalind_revp.txt') as stringfile:
    data = ''.join(stringfile.read().split('\n')[1:])

print(data)

output = open("output.txt", 'w')

for index in range(len(data)):
    for n in range(4,min(13,len(data)+1-index)):
        reverse = list(data[index:index+n])[::-1]
        for i in range(len(reverse)):
            if reverse[i] == "A":
                reverse[i] = "T"
            elif reverse[i] == "T":
                reverse[i] = "A"
            elif reverse[i] == "C":
                reverse[i] = "G"
            elif reverse[i] == "G":
                reverse[i] = "C"
        compl = ''.join(reverse)
        if compl == data[index:index+n]:
            output.write(str(index+1) + ' ' + str(n) + '\n')


output.close()





