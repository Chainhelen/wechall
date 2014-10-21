input_file = open('result_data')
data = []
b = ''
s = ''

for line in input_file:
	d = list(line)
	del d[len(d) - 1]
	for i in range(0,len(d)):
		b += str(d[i])
		if(i % 8 == 7):
			s += chr(int(b,2))
			b = ''
print s
