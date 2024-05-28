import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Кількість випадкових точок для методу Монте-Карло
num_points = 10000

# Згенерувати випадкові точки в межах [a, b]
x_random = np.random.uniform(a, b, num_points)

# Обчислити середнє значення функції у випадкових точках
f_random = f(x_random)
mean_value = np.mean(f_random)

# Обчислити значення інтеграла
integral_mc = (b - a) * mean_value

# Аналітичне обчислення інтеграла
integral_analytical, _ = quad(f, a, b)

# Виведення результатів
print(f"Значення інтеграла методом Монте-Карло: {integral_mc}")
print(f"Аналітичне значення інтеграла: {integral_analytical}")

# Побудова графіка
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()
