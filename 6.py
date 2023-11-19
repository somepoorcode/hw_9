import numpy as np

a = np.arange(16).reshape(4, 4)
print(f"Исходный массив:\n{a}")

a[[1, 3]] = a[[3, 1]]
print(f"\nМассив после замены строк 1 и 3:\n{a}")
