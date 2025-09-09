import numpy as np
import matplotlib.pyplot as plt

# ---------- Definição da circunferência e transformação ----------

# Parâmetros da circunferência
t = np.linspace(0, 2 * np.pi, 200)
x_circle = np.cos(t)
y_circle = np.sin(t)

# Matriz de transformação
A = np.array([[2, 1], 
              [1, 2]])

# Aplicar a transformação
circle_points = np.vstack((x_circle, y_circle))  # Junta x e y em uma matriz 2x200
transformed_points = A @ circle_points

# Extrair coordenadas transformadas
x_transformed = transformed_points[0, :]
y_transformed = transformed_points[1, :]

# ---------- Plotagem ----------

# Criar a visualização
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Configuração para melhor qualidade visual
plt.style.use('default')
plt.rcParams['figure.figsize'] = [10, 5]
plt.rcParams['font.size'] = 12

# Plot da circunferência original
ax1.plot(x_circle, y_circle, 'b-', linewidth=2, label='Circunferência original')
ax1.set_xlim(-3, 3)
ax1.set_ylim(-3, 3)
ax1.set_aspect('equal')
ax1.grid(True, alpha=0.3)
ax1.set_title('Circunferência Original')
ax1.legend()

# Plot da circunferência transformada
ax2.plot(x_transformed, y_transformed, 'r-', linewidth=2, label='Circunferência transformada')
ax2.set_xlim(-3, 3)
ax2.set_ylim(-3, 3)
ax2.set_aspect('equal')
ax2.grid(True, alpha=0.3)
ax2.set_title('Transformação por A = [[2,1],[1,2]]')
ax2.legend()

plt.tight_layout()
plt.show()

# Mostrar informações sobre a transformação
print("Matriz de transformação A:")
print(A)
print("\nA transformação converte a circunferência em uma elipse!")





# python3 -m venv meu_ambiente
# source meu_ambiente/bin/activate
# pip install numpy matplotlib