import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Создаем данные для графиков
x = np.linspace(-3, 3, 50)  # Диапазон X от -3 до 3
y = np.linspace(-3, 3, 50)  # Диапазон Y от -3 до 3
X, Y = np.meshgrid(x, y)    # Создаем сетку координат

# Вычисляем значения функций
Z1 = X**0.25 + Y**0.25      # z = x^0.25 + y^0.25
Z2 = X**2 - Y**2            # z = x^2 - y^2
Z3 = 2*X + 3*Y              # z = 2x + 3y
Z4 = X**2 - Y**2            # z = x^2 - y^2 (дубликат)
Z5 = 2 + 2*X + 2*Y - X**2 - Y**2  # z = 2 + 2x + 2y - x^2 - y^2
# Создаем 3D графики
fig = plt.figure(figsize=(18, 12))

# График 1: z = x^0.25 + y^0.25
ax1 = fig.add_subplot(2, 3, 1, projection='3d')
ax1.plot_surface(X, Y, Z1, cmap='plasma', alpha=0.8)
ax1.set_title('z = x^0.25 + y^0.25')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')

# График 2: z = x^2 - y^2
ax2 = fig.add_subplot(2, 3, 2, projection='3d')
ax2.plot_surface(X, Y, Z2, cmap='plasma', alpha=0.8)
ax2.set_title('z = x² - y²')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')

# График 3: z = 2x + 3y
ax3 = fig.add_subplot(2, 3, 3, projection='3d')
ax3.plot_surface(X, Y, Z3, cmap='plasma', alpha=0.8)
ax3.set_title('z = 2x + 3y')
ax3.set_xlabel('X')
ax3.set_ylabel('Y')
ax3.set_zlabel('Z')

# График 4: z = x^2 - y^2 (дубликат)
ax4 = fig.add_subplot(2, 3, 4, projection='3d')
ax4.plot_surface(X, Y, Z4, cmap='plasma', alpha=0.8)
ax4.set_title('z = x² - y²')
ax4.set_xlabel('X')
ax4.set_ylabel('Y')
ax4.set_zlabel('Z')
# График 5: z = 2 + 2x + 2y - x^2 - y^2
ax5 = fig.add_subplot(2, 3, 5, projection='3d')
ax5.plot_surface(X, Y, Z5, cmap='plasma', alpha=0.8)
ax5.set_title('z = 2 + 2x + 2y - x² - y²')
ax5.set_xlabel('X')
ax5.set_ylabel('Y')
ax5.set_zlabel('Z')

plt.tight_layout()
plt.show()
