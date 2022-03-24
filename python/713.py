for _ in range(int(input())):
	a, b = [int(a) for a in input().split()]
	a, b = int(str(a)[::-1]), int(str(b)[::-1])
	print(int(str(a + b)[::-1]))