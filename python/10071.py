while True:
	try:
		vals = [int(a) for a in input().split()]
	except EOFError:
		break
	print(2*vals[0]*vals[1])