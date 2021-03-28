A = [ [4, 7, 3], [9, 5, 6] ]

for i in range(len(A)):
    for j in range(len(A[i])):
        print(A[i][j], end = ' ')
    print()

for row in A:
    for elem in row:
        print(elem, end = ' ')
    print()