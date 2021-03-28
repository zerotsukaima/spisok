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
        matrix.append([])
        for k in range(t):
            matrix[i].append(random.randint(0, 9))

for i in range(n):
    print("")
    for j in range(m):
        print(" ")
        for j in range(t):
            print(matrix[i][j][k], end = " ")
            if matrix[i][j][k] > maximumElementMatrix:
                maximumElementMatrix = matrix[i][j][k]

for i in range(len(matrix)):
    if matrix[i][j][k] > maximumElementMatrixIndex:
       maximumElementMatrixIndex = matrix[i][j][k]
maxIndex = matrix.index(maximumElementMatrixIndex)

print("\n\nМаксимальный элемент матрицы: ", maximumElementMatrix)
print('\n Индекс: ', maxIndex)

