# not yet finished

for i in range(int(input())):
	C, d = [int(a) for a in input().split()]
	C = (9 / 5) * C + 32
	total = C + d
	total -= 32
	total *= 5/9
	print(f"Case #{i+1}: {round(total, 2) if len(str(total).split('.')[1]) >= 2 else f'{total}0'}")