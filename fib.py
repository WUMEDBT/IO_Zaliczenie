nterms = int(input("Ile liczb? "))

# first two terms
n1, n2 = 0, 1
count = 0

if nterms <= 0:
   print("Prosze podaj liczbe naturalna")

elif nterms == 1:
   print("Sekwencja Fibbonacciego do",nterms,":")
   print(n1)

else:
   print("Sekwencja:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1