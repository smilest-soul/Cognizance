print("Question nmbr 3")
P = [ [1, 'x', 0],
      [2, 'y', 0],
      [3, 'z', 0]]
for i in range(3):
     for j in range(1):
        P[i][j+1]=str(input("Enter the {0} Student Name  ".format( int(i+1) ) ) )
for i in range(3):
     for j in range(1):
        P[i][j+2]=str(input("Enter the {0} Student Marks  ".format( int(i+1) ) ) )
print("{:<10} {:<10} {:<10}".format('Roll no','Name','Marks') )
for i in range(3):
    print(P[0][i],end=" "*10)
print()
for i in range(3):
    print(P[1][i],end=" "*10)
print()
for i in range(3):
    print(P[2][i],end=" "*10)
print()
print("The second row from it is ")
print( P[1][0], P[1][1], P[1][2])