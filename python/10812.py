for _ in range(int(input())):
	s, d = [int(i) for i in input().split()]
	half = s / 2
	dif = d / 2
	a, b = half + dif, half - dif
	if (int(a) == a) and (int(b) == b) and ("-" not in str(a)) and ("-" not in str(b)):
		print(int(a), int(b))
	else:
		print("impossible")