# not yet finishee

a, b, c, d = "`1234567890-=".upper(), 'qwertyuiop[]\\'.upper(), 'asdfghjkl;'.upper(), 'zxcvbnm,./'.upper()

while True:
	try:
		s = input()
	except EOFError:
		break
	for char in a[1:]:
		if char in s:
			s = s.replace(char, a[a.index(char) - 1])
	for char in b[1:]:
		if char in s:
			s = s.replace(char, b[b.index(char) - 1])
	for char in c[1:]:
		if char in s:
			s = s.replace(char, c[c.index(char) - 1])
	for char in d[1:]:
		if char in s:
			s = s.replace(char, d[d.index(char) - 1])
	print(s)