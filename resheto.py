n = int(input("Введите число "))
numbers = [i for i in range(n + 1)]
numbers[1] = 0
newNumbers = []

for i in range(2, n + 1):
    for j in range(i * 2, n + 1, i):
        if numbers[j] != 0:
            numbers[j] = 0
            newNumbers.append(j)

for i in numbers:
    if i == 0:
        numbers.remove(0)
        for j in numbers:
            if j == 0:
                numbers.remove(0)
count = 0
for i in numbers:
    if i % 7 == 0:
        count = i

print(numbers)
print(count)

