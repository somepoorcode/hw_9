import numpy as np


def run_length_encoding(x):
    unique_elements, indices = np.unique(x, return_index=True)
    lengths = np.diff(np.concatenate((indices, [len(x)])))
    return unique_elements, lengths


x = np.array([2, 2, 2, 3, 3, 3, 5])
encoded_values, repetitions = run_length_encoding(x)

print(f"Исходный вектор: {x}\n"
      f"Закодированные значения: {encoded_values}\n"
      f"Количество повторений: {repetitions}")
