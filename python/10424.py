import string
while True:
	try:
		name1, name2 = ''.join(filter(lambda c: c in string.ascii_letters, input())).lower(), ''.join(filter(lambda c: c in string.ascii_letters, input())).lower()
	except EOFError:
		break
	s1, s2 = 0, 0
	for char in name1:
		s1 += string.ascii_lowercase.index(char) + 1
	for char in name2:
		s2 += string.ascii_lowercase.index(char) + 1
	while len(str(s1)) != 1:
		s1 = sum([int(a) for a in str(s1)])
	while len(str(s2)) != 1:
		s2 = sum([int(a) for a in str(s2)])
	if s1 > s2:
		n = round(s2 / s1 * 100, 2)
		print(f"{n}", end = '')
	else:
		n = round(s1 / s2 * 100, 2)
		print(f"{n}", end = '')
	print(f"{0 if str(n).split('.')[1] == '0' else ''} %")