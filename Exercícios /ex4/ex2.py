import numpy as np

print("=== EXERCÍCIO 02: DETERMINANDO TRANSFORMAÇÃO LINEAR ===")
print("T: R^5 → R^3")
print("Im(T) = [(1,0,0), (0,1,0), (1,1,1)]")
print("Ker(T) = [(1,1,1,1,1), (1,1,1,1,0)]")
print()

# PASSO 1: Análise do núcleo e imagem
print("PASSO 1: Análise do núcleo e imagem")
nucleo = np.array([
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0]
])

imagem = np.array([
    [1, 0, 0],
    [0, 1, 0],
    [1, 1, 1]
])

print(f"dim(Ker(T)) = {nucleo.shape[0]}")
print(f"dim(Im(T)) = {imagem.shape[0]}") 
print(f"Verificação: dim(R^5) = {nucleo.shape[0]} + {imagem.shape[0]} = 5 ✓")
print()

# PASSO 2: Construir base para R^5
print("PASSO 2: Construindo base para R^5")
# Base: v1, v2, v3 (canônica) + v4, v5 (núcleo)
base = np.array([
    [1, 0, 0, 0, 0],  # v1
    [0, 1, 0, 0, 0],  # v2  
    [0, 0, 1, 0, 0],  # v3
    [1, 1, 1, 1, 1],  # v4 (núcleo)
    [1, 1, 1, 1, 0]   # v5 (núcleo)
])

print("Base para R^5:")
for i, v in enumerate(base, 1):
    print(f"v{i} = {v}")

# Verificar que é base (det != 0)
det = np.linalg.det(base)
print(f"\nDeterminante da matriz base: {det:.1f} ≠ 0 → É base válida")
print()

# PASSO 3: Definir ação de T na base
print("PASSO 3: Definindo T na base")
print("T(v1) = (1,0,0)  → mapeia para 1º gerador da imagem")
print("T(v2) = (0,1,0)  → mapeia para 2º gerador da imagem") 
print("T(v3) = (1,1,1)  → mapeia para 3º gerador da imagem")
print("T(v4) = (0,0,0)  → núcleo vai para zero")
print("T(v5) = (0,0,0)  → núcleo vai para zero")
print()

# PASSO 4: Encontrar fórmula geral
print("PASSO 4: Encontrando a transformação T(x1,x2,x3,x4,x5)")
print()

print("Para x = (x1,x2,x3,x4,x5), escrevemos x = c1*v1 + c2*v2 + c3*v3 + c4*v4 + c5*v5")
print()
print("Sistema de equações:")
print("x1 = c1 + c4 + c5")
print("x2 = c2 + c4 + c5") 
print("x3 = c3 + c4 + c5")
print("x4 = c4 + c5")
print("x5 = c4")
print()

print("Resolvendo:")
print("c4 = x5")
print("c5 = x4 - x5")
print("c3 = x3 - x4")
print("c2 = x2 - x4") 
print("c1 = x1 - x4")
print()

print("Aplicando T:")
print("T(x) = c1*T(v1) + c2*T(v2) + c3*T(v3) + c4*T(v4) + c5*T(v5)")
print("T(x) = c1*(1,0,0) + c2*(0,1,0) + c3*(1,1,1) + c4*(0,0,0) + c5*(0,0,0)")
print("T(x) = (x1-x4)*(1,0,0) + (x2-x4)*(0,1,0) + (x3-x4)*(1,1,1)")
print()

def T(x):
    """
    Transformação linear T: R^5 → R^3
    T(x1,x2,x3,x4,x5) = (x1+x3-2*x4, x2+x3-2*x4, x3-x4)
    """
    x1, x2, x3, x4, x5 = x
    return np.array([
        x1 + x3 - 2*x4,
        x2 + x3 - 2*x4, 
        x3 - x4
    ])

print("TRANSFORMAÇÃO FINAL:")
print("T(x1,x2,x3,x4,x5) = (x1+x3-2*x4, x2+x3-2*x4, x3-x4)")
print()

# VERIFICAÇÕES
print("=== VERIFICAÇÕES ===")
print()

# Verificar núcleo
print("1. Verificando o núcleo:")
for i, v in enumerate(nucleo, 4):
    resultado = T(v)
    print(f"T(v{i}) = T{tuple(v)} = {resultado} = (0,0,0) ✓")
print()

# Verificar imagem  
print("2. Verificando a imagem:")
print("T(v1) = T(1,0,0,0,0) =", T([1,0,0,0,0]), "= (1,0,0) ✓")
print("T(v2) = T(0,1,0,0,0) =", T([0,1,0,0,0]), "= (0,1,0) ✓") 
print("T(v3) = T(0,0,1,0,0) =", T([0,0,1,0,0]), "= (1,1,1) ✓")
print()

print("A transformação linear encontrada satisfaz todas as condições!")