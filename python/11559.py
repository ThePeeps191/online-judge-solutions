while True:
	try:
		N, B, H, W = [int(a) for a in input().split()]
		hotels = [[int(input()), [int(a) for a in input().split()]] for _ in range(H)]
	except EOFError:
		break
	minimum_cost = B + 1
	for hotel in hotels:
		for bed in hotel[1]:
			if bed >= N:
				cost = N * hotel[0]
				if cost < minimum_cost:
					minimum_cost = cost
	if minimum_cost == B + 1:
		print("stay home")
	else:
		print(minimum_cost)