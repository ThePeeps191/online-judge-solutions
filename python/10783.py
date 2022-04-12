for i in range (int(input())):
	a, b = int(input()), int(input())
	if a % 2 == 0:
		a += 1
	if b % 2 == 0:
		a -= 1
	print(f"Case {i + 1}: {sum(range(a, b + 2, 2))}")