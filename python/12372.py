t = 1
for _ in range(int(input())):
	L, W, H = [int(a) for a in input().split()]
	print(f"Case {t}: {'good' if L <= 20 and W <= 20 and H <= 20 else 'bad'}")
	t += 1