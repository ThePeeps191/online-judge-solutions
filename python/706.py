a, b = 1, 1
while (a != 0) and (b != 0):
	a, b = [int(i) for i in input().split()]
	b1 = str(b)
	output = ["" for _ in range(a)]
	for char in b1:
		if char == "1":
			for line in output:
				