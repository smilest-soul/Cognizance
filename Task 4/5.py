def triangle (S):
	a = S - 1
	for i in range(0, S):
		for j in range(0, a):
			print(end=" ")
		a =a - 1
		for j in range(0, i+1):
			print("* ", end="")
		print("\r")
S = 5
triangle(S)