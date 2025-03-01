import matplotlib.pyplot as plt
import numpy as np

# Генерація випадкових даних
data = np.random.randn(1000)

# Створення гістограми
plt.figure(figsize=(8, 6))
plt.hist(data, bins=30, color='skyblue', edgecolor='black')

# Додавання підписів та заголовка
plt.xlabel('Значення')
plt.ylabel('Частота')
plt.title('Гістограма випадкових чисел')

# Відображення графіка
plt.show()