import random
n = 3
m = 5
t = 7
matrix = []
maximumElementMatrix = 0
maximumElementMatrixIndex = [0]

for i in range(n):
    matrix.append([])
    for j in range(m):
        matrix[i].append([])
        for k in range(t):
            matrix[i][j].append(random.randint(0, 9))

maximumElementMatrix = - 100
for i in range(n):
    for j in range(m):
        for k in range(t):
            if matrix[i][j][k] > maximumElementMatrix:
                maximumElementMatrix = matrix[i][j][k]

inx_x = []
for i in range(n):
    inx_x.append([])
    for j in range(m):
        inx_x[i].append([])
        for k in range(t):
            if matrix[i][j][k] == inx_x:
                print("\n\nМаксимальный элемент матрицы: ", maximumElementMatrix)

for i in range(n):
   print("")
   for j in range(m):
       print(" ")
       for k in range(t):
           print(matrix[i][j][k], end = " ")
