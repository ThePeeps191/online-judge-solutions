x = 1
while True:
	try:
		N = int(input())
		e = [int(a) for a in input().split()]
	except EOFError:
		break
	t = e.count(0)
	print(f"Case {x}: {len(e) - 2 * t}")
	x += 1