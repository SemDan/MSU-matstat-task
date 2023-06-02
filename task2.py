import numpy as np
import pandas as pd
import scipy.stats as stats

from matplotlib import pyplot as plt

# визуализация состоятельности оценки
# получение точек для визуализации
theta = 0.5
rands = np.array([])
x = np.arange(1, 10001)
y = np.array([])
for i in range(0, 10000):
    num = np.random.geometric(theta)
    rands = np.append(rands, num)
    param = 1 / np.mean(rands)
    y = np.append(y, param)

plt.plot(x, y)
plt.axline((0, theta), (1, theta), color='r')
plt.title('theta consistency')
plt.ylabel('theta')
plt.xlabel('dataset size')
plt.show()