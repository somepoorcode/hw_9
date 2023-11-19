import numpy as np


def max_after_zero(x):
    zero_indices = np.where(x == 0)[0]
    next_indices = zero_indices + 1
    valid_next_indices = next_indices[next_indices < len(x)]
    max_value = np.max(x[valid_next_indices])
    return max_value


x = np.array([6, 2, 0, 3, 0, 0, 5, 7, 0])

result = max_after_zero(x)
print(f"Максимальный элемент после нуля: {result}")
