import random
n = int(input("Введите размер матрицы: "))
m = int(input("Введите размер матрицы: "))
matrix = []
counterNegative = counterPositive = 0

for i in range(n):
    matrix.append([])
    for j in range(m):
        matrix[i].append(random.randint(-9, 9))

for i in range(n):
    print("")
    for j in range(m):
        print(matrix[i][j], end = " ")
        if matrix[i][j] > 0:
            counterPositive += 1
        elif matrix[i][j] < 0:
            counterNegative += 1

print("\nКоличество положительных = ", counterPositive)
print("\nКоличество отрицательных = ", counterNegative)