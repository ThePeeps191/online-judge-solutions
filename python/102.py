while True:
	try:
		i = [int(a) for a in input().split()]
	except EOFError:
		break
	bin1 = i[:3]
	bin2 = i[3:6]
	bin3 = i[6:]
	browns = [bin1[0], bin2[0], bin3[0]]
	