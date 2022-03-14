# troops = [1]

# while True:
# 	try:
# 		N = int(input())
# 	except EOFError:
# 		break
# 	if max(troops) >= N:
# 		for element in sorted(troops, reverse=True):
# 			if element > N:
# 				i = troops.index(element) - 2
# 				print(i)
# 				break
# 	else:
# 		while max(troops) < N:
# 			troops.append(troops[-1] + troops.index(troops[-1]) + 2)
# 		troops.append(troops[-1] + troops.index(troops[-1]) + 2)
# 		for element in sorted(troops, reverse=True):
# 			if element > N:
# 				i = troops.index(element)
# 				print(i)
# 				print(troops)
# 				break

# troops = []
# while True:
# 	try:
# 		n = int(input())
# 	except EOFError:
# 		break
# 	r = 1
# 	c = 0
# 	while True:
# 		c += r
# 		r += 1
# 		if c > n:
# 			print(r - 2)
# 			break
# troops = [1]
# while True:
# 	try:
# 		n = int(input())
# 	except EOFError:
# 		break
# 	if max(troops) > n:
# 		for i in range(len(troops)):
# 			if troops[i] > n:
# 				print(i)
# 				break
# 	else:
# 		row = len(troops)
# 		count = troops[-1]
# 		while max(troops) <= n:
# 			count += row
# 			row += 1
# 			troops.append(count)
# 		print(len(troops) - 1)
from math import floor, sqrt
for _ in range(int(input())):
	n = int(input())
	print(f"{floor(sqrt(2 * n + 0.25) + 0.5) - 1}")