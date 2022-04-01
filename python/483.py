while True:
	try:
		s = input().split()
	except EOFError:
		break
	s = [a[::-1] for a in s]
	print(*s)