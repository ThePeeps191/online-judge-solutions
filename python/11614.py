troops = [1]

while True:
	try:
		N = int(input())
	except EOFError:
		break
	if max(troops) >= N:
		for element in sorted(troops, reverse=True):
			if element > N:
				i = troops.index(element) - 2
				print(i)
				break
	else:
		while max(troops) < N:
			troops.append(troops[-1] + troops.index(troops[-1]) + 2)
		troops.append(troops[-1] + troops.index(troops[-1]) + 2)
		for element in sorted(troops, reverse=True):
			if element > N:
				i = troops.index(element)
				print(i)
				print(troops)
				break