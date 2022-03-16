# not yet finished

while True:
	try:
		N, B, H, W = [int(a) for a in input().split()]
		hotels = []
		for _ in range(H):
			hotels.append([int(input()), [int(a) for a in input().split()]])
	except EOFError:
		break
	minimum_cost = None
	for i in range(len(hotels)):
		hotel = hotels[i]
		for week in hotel[1]:
			if week >= N:
				cost = hotel[0] * N
				if cost <= B and (minimum_cost == None or cost < minimum_cost):
					minimum_cost = cost
	print(minimum_cost)