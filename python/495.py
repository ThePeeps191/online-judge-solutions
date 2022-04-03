cache = {}
def fib(n):
	if n in cache:
		return cache[n]
	else:
		if n <= 2:
			cache[n] = 1
			return 1
		else:
			a = fib(n - 1) + fib(n - 2)
			cache[n] = a
			return a
while True:
    try:
        i = int(input())
    except EOFError:
        break
    print(f"The Fibonacci number for {i} is {fib(i)}")