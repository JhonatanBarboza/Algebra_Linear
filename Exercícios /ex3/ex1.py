import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# ---------- Configuração da visualização ----------

# Configurações visuais
plt.style.use('default')
plt.rcParams['figure.figsize'] = [10, 8]
plt.rcParams['font.size'] = 12

# Criar figura 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Criar malha para os planos
y = z = np.linspace(-2, 2, 20)
Y, Z = np.meshgrid(y, z)

# ---------- Plotagem de U, U e U ∩ V ----------

# Definir os planos (subespaços)
# U: x = 0 (plano yz)
# V: y = 0 (plano xz)
# U ∩ V: x = 0 e y = 0 (eixo z)

# Plano U: x = 0 (plano yz)
X_u = np.zeros_like(Y)
ax.plot_surface(X_u, Y, Z, alpha=0.5, color='blue', label='U: x = 0')

# Plano V: y = 0 (plano xz)
x = z = np.linspace(-2, 2, 20)
X, Z = np.meshgrid(x, z)
Y_v = np.zeros_like(X)
ax.plot_surface(X, Y_v, Z, alpha=0.5, color='red', label='V: y = 0')

# Interseção U ∩ V: eixo z (x=0, y=0)
z_axis = np.linspace(-2, 2, 100)
x_axis = np.zeros_like(z_axis)
y_axis = np.zeros_like(z_axis)
ax.plot(x_axis, y_axis, z_axis, 'g-', linewidth=3, label='U ∩ V: eixo z')

# ---------- Finalização do gráfico ----------

# Configurações do gráfico
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_zlim(-2, 2)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Subespaços U, V e U ∩ V em ℝ³')

# Adicionar legenda manualmente (plot_surface não suporta label na legenda)
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor='blue', alpha=0.5, label='U: x = 0 (plano YZ)'),
    Patch(facecolor='red', alpha=0.5, label='V: y = 0 (plano XZ)'),
    Patch(facecolor='green', label='U ∩ V: eixo Z (x=0, y=0)')
]
ax.legend(handles=legend_elements, loc='upper right')

# Adicionar informações textuais
ax.text2D(0.01, 0.90, "U = {(x,y,z) ∈ ℝ³ | x = 0}\nV = {(x,y,z) ∈ ℝ³ | y = 0}\nU ∩ V = {(0,0,z) | z ∈ ℝ}", 
          transform=ax.transAxes, bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.8))

plt.tight_layout()
plt.show()

