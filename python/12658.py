"""
.*. *** ***
.*. ..* ..*
.*. *** ***
.*. *.. ..*
.*. *** ***
"""

output = ''
N = int(input())
nums = [input() for _ in range(5)]
x = 0
for _ in range(N):
	current = ''
	for s in nums:
		current += s[x:x+3]
	x += 4
	if current == '.*..*..*..*..*.':
		output += '1'
	elif current == '***..*****..***':
		output += '2'
	else:
		output += '3'
print(output)