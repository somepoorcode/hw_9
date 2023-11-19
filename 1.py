import numpy as np

with open('1_input.txt', 'r') as file:
    lines = file.readlines()

a = []
for line in lines:
    row = [int(num) for num in line.strip().split(',')]
    a.append(row)
matrix = np.array(a)

print(f"Сумма всех элементов: {np.sum(matrix)}\n"
      f"Максимальный элемент: {np.max(matrix)}\n"
      f"Минимальный элемент: {np.min(matrix)}")
