s = []
while True:
	try:
		s.append(input())
	except EOFError:
		break
s = s[::-1]
for i in range(max([len(a) for a in s])):
	o = ''
	for string in s:
		if len(string) >= i + 1:
			o += string[i]
	print(o)