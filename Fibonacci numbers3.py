# Python Program for Fibonacci numbers.

nterms = int(input("Please enter the number of terms  "))

# the first two terms are always the same.
n1, n2 = 0, 1
i = 0

# In case of negative or invalid input.
if nterms <= 0:
   nterms = int(input("Input invalid.Please enter a positive integer  "))
   print("Fibonacci sequence:")
   while i < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       i += 1

elif nterms == 1:
   print("Fibonacci sequence:")
   print(n1)
else:
   print("Fibonacci sequence:")
   while i < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       i += 1
