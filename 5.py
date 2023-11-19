import numpy as np
from scipy.stats import multivariate_normal
import time


def log_density(X, m, C):
    D = len(m)
    det_C = np.linalg.det(C)
    inv_C = np.linalg.inv(C)
    norm_factor = -0.5 * D * np.log(2 * np.pi) - 0.5 * np.log(det_C)

    diff = X - m
    exponent = -0.5 * np.sum(diff @ inv_C * diff, axis=1)

    log_density_vals = norm_factor + exponent
    return log_density_vals


np.random.seed(42)
N = 10
D = 3
X = np.random.randn(N, D)
m = np.random.randn(D)
C = np.random.randn(D, D)
C = C @ C.T

start_time = time.time()
result_custom = log_density(X, m, C)
custom_duration = time.time() - start_time

start_time = time.time()
result_scipy = multivariate_normal(m, C).logpdf(X)
scipy_duration = time.time() - start_time

print(f"Numpy:\n"
      f"Логарифм плотности:\n{result_custom}\n"
      f"Время выполнения: {custom_duration}\n"
      f"\nscipy.stats.multivariate_normal:\n"
      f"Логарифм плотности\n{result_scipy}\n"
      f"Время выполнения: {scipy_duration}")
