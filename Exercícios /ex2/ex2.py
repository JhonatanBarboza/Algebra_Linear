import numpy as np
from numpy.linalg import inv

# Definindo as bases
B = np.column_stack(([1, 0, 1], [1, 1, 1], [1, 1, 2]))
C = np.eye(3)  # Base canônica

# Matrizes de mudança de base
M_B_C = np.dot(inv(C), B)  # = B
M_C_B = np.dot(inv(B), C)  # = B^(-1)

# Conversão de coordenadas
v_C = np.array([8, 7, 1])
v_B = np.dot(M_C_B, v_C)

print("M_B^C (B para C):")
print(M_B_C)
print("\nM_C^B (C para B):")
print(M_C_B)
print(f"\nCoordenadas de v na base C: {v_C}")
print(f"Coordenadas de v na base B: {v_B}")