while True:
	n = int(input())
	if n == 0:
		break
	while True:
		s = sum([int(a) for a in str(n)])
		n = s
		if len(str(s)) == 1:
			print(s)
			break