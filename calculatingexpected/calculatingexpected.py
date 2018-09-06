
with open('rosalind_iev.txt') as stringfile:
    s = stringfile.read().split()


ex = ((int(s[0])*1) + (int(s[1])*1) + (int(s[2])*1) + (int(s[3])*0.75) + (int(s[4])*0.5))*2


output = open("output.txt", 'w')
output.write(str(ex))
output.close()
