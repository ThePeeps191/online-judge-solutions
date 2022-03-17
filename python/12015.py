for i in range(int(input())):
	urls = [input().split() for _ in range(10)]
	rating = max([int(a[1]) for a in urls])
	print(f"Case #{i + 1}:")
	for u in urls:
		if int(u[1]) == rating:
			print(u[0])