"""
Exercício 6 - Normas em R² e Processo de Gram-Schmidt
Implementação simples dos exercícios de monitoria
"""

import numpy as np
import matplotlib.pyplot as plt

print("=== EXERCÍCIO 1: NORMAS EM R² ===")
print()

# Exercício 1: Visualização das normas em R²
def norma_euclidiana(x, y):
    """Norma euclidiana (L2): ||x||₂ = √(x² + y²)"""
    return np.sqrt(x**2 + y**2)

def norma_soma(x, y):
    """Norma da soma (L1): ||x||₁ = |x| + |y|"""
    return np.abs(x) + np.abs(y)

def norma_maximo(x, y):
    """Norma do máximo (L∞): ||x||∞ = max(|x|, |y|)"""
    return np.maximum(np.abs(x), np.abs(y))

# Criar grid de pontos
theta = np.linspace(0, 2*np.pi, 1000)

# Círculo unitário para norma euclidiana (||x||₂ = 1)
x_euclidiana = np.cos(theta)
y_euclidiana = np.sin(theta)

# Losango para norma da soma (||x||₁ = 1)
# |x| + |y| = 1 → vértices em (±1,0) e (0,±1)
x_soma = np.array([1, 0, -1, 0, 1])
y_soma = np.array([0, 1, 0, -1, 0])

# Quadrado para norma do máximo (||x||∞ = 1)
# max(|x|, |y|) = 1 → quadrado com vértices em (±1,±1)
x_maximo = np.array([1, 1, -1, -1, 1])
y_maximo = np.array([1, -1, -1, 1, 1])

# Plotar as três normas
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Norma euclidiana
axes[0].plot(x_euclidiana, y_euclidiana, 'b-', linewidth=2, label='||x||₂ = 1')
axes[0].grid(True, alpha=0.3)
axes[0].set_xlim(-1.5, 1.5)
axes[0].set_ylim(-1.5, 1.5)
axes[0].set_aspect('equal')
axes[0].set_title('Norma Euclidiana (L₂)', fontweight='bold')
axes[0].set_xlabel('x')
axes[0].set_ylabel('y')
axes[0].legend()

# Norma da soma
axes[1].plot(x_soma, y_soma, 'r-', linewidth=2, label='||x||₁ = 1')
axes[1].fill(x_soma, y_soma, 'red', alpha=0.2)
axes[1].grid(True, alpha=0.3)
axes[1].set_xlim(-1.5, 1.5)
axes[1].set_ylim(-1.5, 1.5)
axes[1].set_aspect('equal')
axes[1].set_title('Norma da Soma (L₁)', fontweight='bold')
axes[1].set_xlabel('x')
axes[1].set_ylabel('y')
axes[1].legend()

# Norma do máximo
axes[2].plot(x_maximo, y_maximo, 'g-', linewidth=2, label='||x||∞ = 1')
axes[2].fill(x_maximo, y_maximo, 'green', alpha=0.2)
axes[2].grid(True, alpha=0.3)
axes[2].set_xlim(-1.5, 1.5)
axes[2].set_ylim(-1.5, 1.5)
axes[2].set_aspect('equal')
axes[2].set_title('Norma do Máximo (L∞)', fontweight='bold')
axes[2].set_xlabel('x')
axes[2].set_ylabel('y')
axes[2].legend()

plt.tight_layout()
plt.show()

print("Geometricamente:")
print("• Norma euclidiana (L₂): Círculo unitário")
print("• Norma da soma (L₁): Losango (diamante)")
print("• Norma do máximo (L∞): Quadrado")
print()

print("=== EXERCÍCIO 2: PROCESSO DE GRAM-SCHMIDT ===")
print()

# Exercício 2: Processo de Gram-Schmidt
def gram_schmidt(vectors):
    """
    Implementa o processo de ortogonalização de Gram-Schmidt
    
    Args:
        vectors: matriz onde cada coluna é um vetor da base original
    
    Returns:
        orthonormal_basis: matriz com base ortonormal (cada coluna é um vetor)
    """
    n = vectors.shape[1]  # número de vetores
    orthogonal = np.zeros_like(vectors, dtype=float)
    orthonormal = np.zeros_like(vectors, dtype=float)
    
    for i in range(n):
        # Começar com o vetor original
        v = vectors[:, i].astype(float)
        
        # Subtrair as projeções nos vetores já ortogonalizados
        for j in range(i):
            # Projeção de v sobre u_j
            u_j = orthogonal[:, j]
            proj = np.dot(v, u_j) / np.dot(u_j, u_j) * u_j
            v = v - proj
        
        # Armazenar vetor ortogonal
        orthogonal[:, i] = v
        
        # Normalizar para obter vetor ortonormal
        norm = np.linalg.norm(v)
        if norm > 1e-10:  # evitar divisão por zero
            orthonormal[:, i] = v / norm
        else:
            print(f"Aviso: Vetor {i+1} é linearmente dependente dos anteriores")
    
    return orthonormal

# Gerar base do R¹⁰ (mesmo código do notebook)
np.random.seed(42)

# Começar com a matriz identidade
I = np.identity(10, dtype=int)

# Adicionar pequenas perturbações inteiras
perturbation = np.random.randint(-3, 4, size=(10, 10))
B_int = I + perturbation

# Verificar se os vetores são linearmente independentes
rank = np.linalg.matrix_rank(B_int)
print(f"Rank da matriz: {rank}")

if rank == 10:
    print("✓ Os vetores são linearmente independentes")
    print()
    
    # Mostrar alguns vetores da base original
    print("Base original B (primeiros 10 vetores):")
    for i in range(10):
        print(f"v{i+1} = {B_int[:, i]}")
    print()
    
    # Aplicar Gram-Schmidt
    print("Aplicando processo de Gram-Schmidt...")
    base_ortonormal = gram_schmidt(B_int)
    
    print("✓ Base ortonormal obtida!")
    print()
    
    # Mostrar alguns vetores da base ortonormal
    print("Base ortonormal (primeiros 10 vetores):")
    for i in range(10):
        vetor = base_ortonormal[:, i]
        print(f"u{i+1} = [{vetor[0]:.3f}, {vetor[1]:.3f}, {vetor[2]:.3f}, {vetor[3]:.3f}, {vetor[4]:.3f}, {vetor[5]:.3f}, {vetor[6]:.3f}, {vetor[7]:.3f}, {vetor[8]:.3f}, {vetor[9]:.3f}]")
    print()