#формируем последовательность псевдослучайных чисел
from random import randint
numericList = [randint(-10, 10) for p in range(0, 20)]

print("Начальный список случайных чисел: ", numericList)
#вывожу максимальный элемент списка
max(numericList)
print("Максимальный элемент списка: ", max(numericList))

for j in numericList:
    if j == 0:
        numericList.remove(0)
        numericList.insert(max(numericList) + 1, 0)
        continue

print("Cписок псевдослучайных чисел после решения задачи: ", numericList)


