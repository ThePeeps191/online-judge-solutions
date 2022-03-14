t = 1
for _ in range(int(input())):
	N = int(input())
	high, low = 0, 0
	walls = [int(a) for a in input().split()]
	for wall in range(len(walls) - 1):
		w = walls[wall]
		next_wall = walls[wall + 1]
		if w > next_wall:
			low += 1
		elif next_wall > w:
			high += 1
	print(f"Case {t}: {high} {low}")
	t += 1