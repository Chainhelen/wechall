data = []
li = []

data.append(open('data2_1').read())
data.append(open('data2_2').read())
data.append(open('data2_3').read())

for i in range(0,len(data)):
	temp = list(data[i])
	del temp[len(data[i]) - 1]
	li.append(temp)

def fu(nr1,nr2):
	result = []
	for i in range(0,len(nr1)):
		result.append(str((int)(nr1[i]) ^ (int)(nr2[i])))
	return result

result = fu(fu(li[1],li[0]),li[2])
s = ''
b = []

for i in range(0,len(result)):
	b.append(result[i])
	if(i % 8 == 7):
		s += chr(int(''.join(b),2))	
		b = []

print s
