import numpy as np

# Exercício 02: Transformação linear que mapeia v=[1,1,1,1,1] nele mesmo

# Vetor v
v = np.array([1, 1, 1, 1, 1])
print("Vetor v:", v)

# A solução mais simples: matriz identidade 5x5
A = np.eye(5)
print("\nMatriz A (identidade 5x5):")
print(A)

# Verificando que A*v = v
resultado = A @ v
print("\nA * v =", resultado)
print("v =    ", v)
print("A*v == v?", np.allclose(resultado, v))