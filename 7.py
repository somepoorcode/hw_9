import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')

species_column = iris[:, -1]
unique_species, species_counts = np.unique(species_column, return_counts=True)

print(f"Уникальные значения в столбце species: {unique_species}\n"
      f"Количество каждого уникального значения: {species_counts}")
