text = input()

print("Ilość słow: ", len(text.split(" ")))
print("Liczba słów: ", len(text.replace(" ", " ")))

c = 0
for char in text:
	if char.isalnum():
	c += 1
	
print("Znaki alfanumeryczne: ", c)