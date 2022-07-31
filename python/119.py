while True:
	try:
		T = int(input())
	except EOFError:
		break
	names = input().split()
	gifts = {a : 0 for a in names}
	for _ in range(T):
		guy = input().split()
		name = guy[0]
		give = int(guy[1])
		if give == 0:
			continue
		del guy[0]
		del guy[0]
		gifts[name] -= give
		total = int(guy[0])
		del guy[0]
		gives_each = give // total
		gifts[name] += give - gives_each * total
		for person in guy:
			gifts[person] += gives_each
	for name in gifts:
		print(name, gifts[name])
	print()