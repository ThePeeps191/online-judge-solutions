import sys
input = sys.stdin.readline

while True:
	n = int(input())
	if n == 0: break
	print(*sorted([int(a) for a in input().split()]))