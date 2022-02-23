P=str( input("Enter the string:-") )
even=""
for S in range(len(P)):
    if S%2==0:
        even= even+P[S]
print(even)
