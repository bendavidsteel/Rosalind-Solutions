maxlen = 2
maxstring = ""

def jloop


with open('sample.txt') as stringfile:
    data = stringfile.read().split('\n')[1::2]


for i in range(len(min(data, key=len))):
    for n in range(maxlen, len(min(data, key=len))):
        for j in range(1, len(data)):
            print(j)
            print(data[0][i:i+n])
            print(data[j][i:i+n])
            if data[0][i:i+n] != data[j][i:i+n]:
                break
        else:
            continue
            if n > maxlen:
                maxlen = n
                maxstring = data[0][i:i+n]
        break





output = open("output.txt", 'w')
output.write(maxstring)
output.close()

