size = int(input("Podaj wielkość: "))

for a in range(1, size +1):
	for b in range(1, size + 1):
		print(a * b, end=" ")
	print()