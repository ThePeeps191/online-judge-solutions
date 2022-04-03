def factors(x):
	result = []
	i = 1
	while i*i <= x:
		if x % i == 0:
			result.append(i)
			if x//i != i:
				result.append(x//i)
		i += 1
	return result

for _ in range(int(input())):
    a, b = [int(i) for i in input().split()]
    m = 0
    x = 0
    for i in range(a, b + 1):
        result = factors(i)
        if len(result) > m:
            m = len(result)
            x = i
    print(f"Between {a} and {b}, {x} has a maximum of {m} divisors.")