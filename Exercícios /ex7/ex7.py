"""
Exercício 7 - Isometrias no Plano via Matrizes (Versão Simples)
"""

import numpy as np
import matplotlib.pyplot as plt

# Triângulo ABC: A=(1,1), B=(3,1), C=(2,3)
T = np.array([[1, 3, 2],
              [1, 1, 3]])

print("Triângulo original T:")
print(T)

# Matrizes das transformações
print("\n=== MATRIZES DE TRANSFORMAÇÃO ===")

# a) Reflexão no eixo x
Rx = np.array([[1, 0], [0, -1]])
print("Reflexão eixo x:")
print(Rx)

# b) Reflexão na reta y = x  
Ry_x = np.array([[0, 1], [1, 0]])
print("Reflexão y = x:")
print(Ry_x)

# c) Rotação 90° anti-horária
R90 = np.array([[np.cos(np.pi/2), -np.sin(np.pi/2)], [np.sin(np.pi/2), np.cos(np.pi/2)]])
print("Rotação 90°:")
print(R90)

print("\n=== APLICAÇÕES ===")

# Aplicar transformações
T1 = Rx @ T
print("Após reflexão x:")
print(T1)

T2 = Ry_x @ T  
print("Após reflexão y=x:")
print(T2)

T3 = R90 @ T
print("Após rotação 90°:")
print(T3)

# d) Translação por v = (2, -1)
v = np.array([[2], [-1]])
T4 = T + v
print("Após translação (2,-1):")
print(T4)

# Função para plotar triângulos
def plotar_triangulo(matriz, titulo, cor='blue', ax=None):
    """Plota um triângulo a partir da matriz de coordenadas"""
    if ax is None:
        fig, ax = plt.subplots(1, 1, figsize=(6, 6))
    
    # Extrair pontos (cada coluna é um ponto)
    pontos = matriz.T
    # Fechar o triângulo conectando ao primeiro ponto
    x_coords = np.append(pontos[:, 0], pontos[0, 0])
    y_coords = np.append(pontos[:, 1], pontos[0, 1])
    
    ax.plot(x_coords, y_coords, 'o-', color=cor, linewidth=2, markersize=8)
    ax.fill(x_coords, y_coords, color=cor, alpha=0.3)
    
    # Marcar vértices
    labels = ['A', 'B', 'C']
    for i, (x, y) in enumerate(pontos):
        ax.annotate(labels[i], (x, y), xytext=(8, 8), 
                   textcoords='offset points', fontsize=12, fontweight='bold')
    
    ax.grid(True, alpha=0.3)
    ax.set_aspect('equal')
    ax.set_title(titulo, fontsize=14, fontweight='bold')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    
    return ax

# Criar visualização com todas as transformações

fig, ax = plt.subplots(1, 1, figsize=(12, 10))

# Plotar todas as transformações
plotar_triangulo(T, "Original", 'blue', ax)
plotar_triangulo(T1, "Reflexão X", 'red', ax)
plotar_triangulo(T2, "Reflexão Y=X", 'green', ax)
plotar_triangulo(T3, "Rotação 90°", 'orange', ax)
plotar_triangulo(T4, "Translação", 'purple', ax)

# Adicionar linhas de referência
ax.axhline(y=0, color='gray', linestyle='--', alpha=0.5)
ax.axvline(x=0, color='gray', linestyle='--', alpha=0.5)
x_line = np.linspace(-4, 6, 100)
ax.plot(x_line, x_line, 'gray', linestyle='--', alpha=0.3, label='y=x')

ax.set_xlim(-4, 6)
ax.set_ylim(-4, 4)
ax.set_title('Todas as Transformações do Triângulo', fontsize=16, fontweight='bold')
ax.legend(['Original', '', 'Reflexão X', '', 'Reflexão Y=X', '', 
          'Rotação 90°', '', 'Translação', ''])
plt.tight_layout()
plt.show()