input_file = []
data = []
b = []
m=""

input_file1=open('data1')
input_file2=open('data2')
input_file3=open('data3')
input_file4=open('data4','w')

data.append(input_file1.read().strip(' '))
data.append(input_file2.read().strip(' '))
data.append(input_file3.read().strip(' '))

def bitor(nr1, nr2):
	result = []
	for i in range(0,len(nr1)):
		if(str(nr1[i]).isdigit()):
			result.append(str((int)(nr1[i]) | (int)(nr2[i])))
	return result

result = bitor(bitor(data[0],data[1]),data[2])

for i in range(0,len(result)):
	b.append(result[i])
	if (i % 8 == 7):
		s = str(''.join(b))
		m += chr(int(s,2))
   		b = []
print m
