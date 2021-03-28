n = int(input("Введите число "))
numbers = [i for i in range(n + 1)]
numbers[0] = 0
newNumbers = []

for i in range(1, n + 1):
    for j in range(i, n + 1):
        if numbers[j] != 0 and numbers[j] % 7 != 0:
            numbers[j] = 0
            newNumbers.append(j)

for i in numbers:
    if i == 0:
        numbers.remove(0)
        for j in numbers:
            if j == 0:
                numbers.remove(0)
                for k in numbers:
                    if k == 0:
                        numbers.remove(0)

print(numbers)

