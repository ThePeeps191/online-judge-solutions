while True:
	try:
		a, b = [int(i) for i in input().split()]
	except EOFError:
		break
	print(abs(b - a))