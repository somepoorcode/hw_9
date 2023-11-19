import numpy as np

array = np.random.randn(10, 4)
a = array[:5, :]

print(f"Массив случайных чисел нормального распределения 10x4:\n{array}\n"
      f"Минимальное значение:\n{np.min(array)}\n"
      f"Максимальное значение:\n{np.max(array)}\n"
      f"Средние значения по столбцам:\n{np.mean(array, axis=0)}\n"
      f"Стандартное отклонение: {np.std(array)}\n"
      f"Первые 5 строк:\n{a}")
