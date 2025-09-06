import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(1000)

plt.figure(figsize=(8, 6))
plt.hist(data, bins=30, color='skyblue', edgecolor='black')

plt.xlabel('Значення')
plt.ylabel('Частота')
plt.title('Гістограма випадкових чисел')

plt.show()
