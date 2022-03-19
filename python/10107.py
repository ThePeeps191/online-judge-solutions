import statistics
import math
nums = []
while True:
	try:
		n = int(input())
	except EOFError:
		break
	nums.append(n)
	print(math.floor(statistics.median(nums)))