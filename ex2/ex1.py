import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Vetores base
u = np.array([1, 0, 1])
v = np.array([0, 1, 1])

# Criar figura 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Criar plano x + y - z = 0
x_plane = np.linspace(-3, 3, 20)
y_plane = np.linspace(-3, 3, 20)
X_plane, Y_plane = np.meshgrid(x_plane, y_plane)
Z_plane = X_plane + Y_plane
ax.plot_surface(X_plane, Y_plane, Z_plane, alpha=0.3, color='lightblue')

# Plotar vetores base
origin = np.array([0, 0, 0])
ax.quiver(origin[0], origin[1], origin[2], u[0], u[1], u[2], color='red', arrow_length_ratio=0.1, linewidth=3, label='u = [1,0,1]')
ax.quiver(origin[0], origin[1], origin[2], v[0], v[1], v[2], color='blue', arrow_length_ratio=0.1, linewidth=3, label='v = [0,1,1]')

# Gerar e plotar combinações lineares
np.random.seed(42)
for _ in range(10):
    a, b = np.random.uniform(-2, 2, 2)
    w = a * u + b * v
    ax.quiver(origin[0], origin[1], origin[2], w[0], w[1], w[2], color='green', arrow_length_ratio=0.1, alpha=0.6, linewidth=1)

# Configurações do gráfico
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Subespaço gerado por u e v\nPlano: x + y - z = 0')
ax.set_xlim([-3, 3])
ax.set_ylim([-3, 3])
ax.set_zlim([-3, 3])
ax.legend()

plt.tight_layout()
plt.show()