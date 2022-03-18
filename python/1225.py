for _ in range(int(input())):
	n = int(input())
	s = ''.join([str(a) for a in range(1, n + 1)])
	o = ''
	for i in '0123456789':
		o += str(s.count(i)) + " "
	print(o[:-1])