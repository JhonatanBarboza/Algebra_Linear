import numpy as np
from numpy.linalg import svd

# Matriz de avaliações original (10 usuários x 8 filmes)
R = np.array([
    [5, 3, 0, 1, 0, 0, 0, 2],
    [4, 0, 0, 1, 2, 0, 0, 0],
    [1, 1, 0, 5, 0, 0, 0, 0],
    [0, 0, 5, 4, 0, 0, 0, 0],
    [3, 0, 0, 0, 4, 0, 0, 5],
    [0, 2, 4, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 3, 5, 2],
    [2, 0, 3, 0, 0, 0, 0, 4],
    [0, 0, 0, 0, 0, 5, 4, 0],
    [1, 2, 0, 0, 0, 0, 3, 0]
])

print("Matriz original:")
print(R)
print("\n" + "="*50 + "\n")

# 1. Pré-processamento: substituir zeros pela média da linha (usuário)
R_filled = R.copy().astype(float)

for i in range(R.shape[0]):  # Para cada usuário
    row = R[i]
    # Calcular média apenas dos valores não-zero
    non_zero_values = row[row > 0]
    if len(non_zero_values) > 0:
        media_usuario = np.mean(non_zero_values)
        # Substituir zeros pela média do usuário
        R_filled[i][R[i] == 0] = media_usuario

print("Matriz preenchida com médias dos usuários:")
print(np.round(R_filled, 2))
print("\n" + "="*50 + "\n")

# 2. Aplicar SVD
U, S, VT = svd(R_filled, full_matrices=False)

# 3. Reconstruir com k=3 componentes principais
k = 3
S_k = np.diag(S[:k])
U_k = U[:, :k]
VT_k = VT[:k, :]

# Reconstruir a matriz
R_hat = U_k @ S_k @ VT_k

# Limitar valores entre 1 e 5
R_hat_clipped = np.clip(R_hat, 1, 5)

print("Matriz reconstruída (com valores limitados entre 1-5):")
print(np.round(R_hat_clipped, 2))
print("\n" + "="*50 + "\n")

# 4. Gerar recomendações
print("RECOMENDAÇÕES DE FILMES:")
print("="*30)

# Para cada usuário
for i in range(R.shape[0]):
    usuario = i + 1
    
    # Encontrar filmes não avaliados (zeros na matriz original)
    filmes_nao_avaliados = np.where(R[i] == 0)[0]
    
    if len(filmes_nao_avaliados) > 0:
        # Pegar as notas previstas para filmes não avaliados
        notas_previstas = R_hat_clipped[i][filmes_nao_avaliados]
        
        # Ordenar por nota prevista (decrescente)
        indices_ordenados = np.argsort(notas_previstas)[::-1]
        
        # Recomendar os top 2 filmes
        top_2 = indices_ordenados[:2]
        
        print(f"Usuário {usuario}:")
        for j, idx in enumerate(top_2):
            filme_id = filmes_nao_avaliados[idx] + 1  # +1 para F1, F2, etc.
            nota_prevista = notas_previstas[idx]
            print(f"  {j+1}º lugar: Filme F{filme_id} (nota prevista: {nota_prevista:.2f})")
        print()
    else:
        print(f"Usuário {usuario}: Já avaliou todos os filmes!")
        print()

print("="*50)
print("Sistema de recomendação concluído!")