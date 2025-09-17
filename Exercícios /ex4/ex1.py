import numpy as np
import matplotlib.pyplot as plt
import math

print("=== EXERCÍCIO 01: TRANSFORMAÇÃO LINEAR ===")
print("T: R² → R² tal que T(1,0) = (cos θ, sen θ) e T(0,1) = (-sen θ, cos θ)")
print()

# PARTE 1: Determine a transformação T e sua matriz na base canônica
print("PARTE 1: Determinando a transformação T e sua matriz")
print()

print("1. Vetor genérico:")
print("   Qualquer vetor (x,y) ∈ R² pode ser escrito como:")
print("   (x,y) = x·(1,0) + y·(0,1) = x·e₁ + y·e₂")
print()

print("2. Aplicando linearidade:")
print("   T(x,y) = T(x·e₁ + y·e₂) = x·T(e₁) + y·T(e₂)")
print()

print("3. Substituindo os valores dados:")
print("   T(e₁) = T(1,0) = (cos θ, sen θ)")
print("   T(e₂) = T(0,1) = (-sen θ, cos θ)")
print()

print("4. Resultado da transformação:")
print("   T(x,y) = x·(cos θ, sen θ) + y·(-sen θ, cos θ)")
print("   T(x,y) = (x cos θ - y sen θ, x sen θ + y cos θ)")
print()

print("5. Matriz na base canônica:")
print("   As colunas são T(e₁) e T(e₂):")
print("   [T] = [cos θ  -sen θ]")
print("         [sen θ   cos θ]")
print()

# PARTE 2: Implementar função que retorna a matriz
def matriz_transformacao(theta):
    """
    Retorna a matriz da transformação T para um ângulo theta.
    [T] = [cos θ  -sen θ]
          [sen θ   cos θ]
    """
    return np.array([
        [math.cos(theta), -math.sin(theta)],
        [math.sin(theta), math.cos(theta)]
    ])

def aplicar_transformacao(pontos, theta):
    """
    Aplica a transformação T nos pontos dados.
    """
    T = matriz_transformacao(theta)
    return np.dot(pontos, T.T)  # Multiplica pontos por T transposta

print("PARTE 2: Função implementada ✓")
print()

# PARTE 3: Aplicar no triângulo com θ = π/4
print("PARTE 3: Aplicando no triângulo com θ = π/4")
print()

theta = math.pi / 4
cos_theta = math.cos(theta)
sen_theta = math.sin(theta)

print(f"Para θ = π/4:")
print(f"cos(π/4) = √2/2 ≈ {cos_theta:.3f}")
print(f"sen(π/4) = √2/2 ≈ {sen_theta:.3f}")
print()

# Matriz para θ = π/4
T_matrix = matriz_transformacao(theta)
print("Matriz de transformação:")
print(f"[T] = [{cos_theta:.3f}  {-sen_theta:.3f}]")
print(f"      [{sen_theta:.3f}   {cos_theta:.3f}]")
print()

# Vértices originais do triângulo
vertices_originais = np.array([
    [-1, 1],   # P = (-1, 1)
    [1, 1],    # Q = (1, 1)  
    [0, 1],    # R = (0, 1)
    [-1, 1]    # Fechar o triângulo
])

print("Vértices originais:")
print("P = (-1, 1)")
print("Q = (1, 1)")
print("R = (0, 1)")
print()

# Aplicar transformação
vertices_transformados = aplicar_transformacao(vertices_originais, theta)

print("Calculando novos vértices:")
print()

# Cálculo detalhado para cada vértice
vertices = [("P", [-1, 1]), ("Q", [1, 1]), ("R", [0, 1])]

for nome, (x, y) in vertices:
    print(f"Para {nome} = ({x}, {y}):")
    print(f"T({x},{y}) = ({x}·cos θ - {y}·sen θ, {x}·sen θ + {y}·cos θ)")
    
    novo_x = x * cos_theta - y * sen_theta
    novo_y = x * sen_theta + y * cos_theta
    
    print(f"T({x},{y}) = ({x}·{cos_theta:.3f} - {y}·{sen_theta:.3f}, {x}·{sen_theta:.3f} + {y}·{cos_theta:.3f})")
    print(f"T({x},{y}) = ({novo_x:.3f}, {novo_y:.3f})")
    
    # Valores exatos
    if nome == "P":
        print(f"P' = (-√2, 0) ≈ ({-math.sqrt(2):.3f}, 0)")
    elif nome == "Q":
        print(f"Q' = (0, √2) ≈ (0, {math.sqrt(2):.3f})")
    elif nome == "R":
        print(f"R' = (-√2/2, √2/2) ≈ ({-math.sqrt(2)/2:.3f}, {math.sqrt(2)/2:.3f})")
    print()

# Visualização
plt.figure(figsize=(12, 10))

# Triângulo original
plt.plot(vertices_originais[:, 0], vertices_originais[:, 1], 'b-o', 
         label='Triângulo Original', linewidth=2, markersize=8)

# Triângulo transformado
plt.plot(vertices_transformados[:, 0], vertices_transformados[:, 1], 'r-o', 
         label='Triângulo Transformado (θ=π/4)', linewidth=2, markersize=8)

# Eixos coordenados
plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
plt.axvline(x=0, color='k', linestyle='-', alpha=0.3)

# Configurações do gráfico
plt.grid(True, alpha=0.3)
plt.axis('equal')
plt.legend(fontsize=12)
plt.title('Transformação Linear T - Rotação de π/4 radianos (45°)', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)

# Adicionar anotações dos pontos
for i, (nome, _) in enumerate(vertices):
    # Pontos originais
    plt.annotate(nome, vertices_originais[i], xytext=(5, 5), 
                textcoords='offset points', color='blue', fontsize=10)
    # Pontos transformados  
    plt.annotate(nome+"'", vertices_transformados[i], xytext=(5, 5),
                textcoords='offset points', color='red', fontsize=10)

plt.tight_layout()
plt.show()
