n = int(input('Введите число до которого хотите найти все простые числа: '))
numbers = list(range(2, n + 1))

for i in numbers:
    if i != 0:
        for j in range(2 * i, n + 1, i):
            numbers[j - 2] = 0

print(numbers)