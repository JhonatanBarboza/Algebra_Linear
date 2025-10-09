"""
SVD2.py - Compressão de Imagem (Versão Essencial)
Demonstra como usar SVD para comprimir imagens mantendo qualidade visual
"""

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# === PASSO 1: CARREGAR E PREPARAR A IMAGEM ===
# Carregar a imagem e converter para tons de cinza (escala 0-255)
img = Image.open("tuc.jpg").convert('L')  # 'L' = Luminance (tons de cinza)
matriz = np.array(img)  # Converter para matriz numpy

print(f"Dimensões da imagem: {matriz.shape}")
print(f"Valores na matriz: {matriz.min()} a {matriz.max()}")

# === PASSO 2: APLICAR DECOMPOSIÇÃO SVD ===
# SVD decompõe a matriz A em: A = U × S × V^T
# U: matriz ortogonal (vetores singulares à esquerda)
# s: valores singulares (diagonal, em ordem decrescente)
# Vt: matriz ortogonal transposta (vetores singulares à direita)
U, s, Vt = np.linalg.svd(matriz, full_matrices=False)

print(f"Forma de U: {U.shape}")
print(f"Número de valores singulares: {len(s)}")
print(f"Forma de Vt: {Vt.shape}")

# === PASSO 3: COMPRESSÃO (50%) ===
# Manter apenas os primeiros k valores singulares mais importantes
k = len(s) // 2  # 50% dos componentes (divisão inteira)
print(f"Mantendo {k} de {len(s)} componentes")

# Reconstruir a imagem usando apenas os k primeiros componentes
# Fórmula: A_aproximada = U[:, :k] × S_k × Vt[:k, :]
img_comprimida = U[:, :k] @ np.diag(s[:k]) @ Vt[:k, :]

# Garantir que os valores permaneçam no intervalo válido [0, 255]
img_comprimida = np.clip(img_comprimida, 0, 255)

# === PASSO 4: VISUALIZAÇÃO ===
# Criar figura com 2 subplots lado a lado
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Imagem original (esquerda)
ax1.imshow(matriz, cmap='gray', vmin=0, vmax=255)
ax1.set_title('Imagem Original', fontsize=14, fontweight='bold')
#ax1.axis('off')  # Remover eixos para melhor visualização

# Imagem comprimida (direita)
ax2.imshow(img_comprimida, cmap='gray', vmin=0, vmax=255)
ax2.set_title(f'Comprimida 50%\n({k}/{len(s)} componentes SVD)', 
              fontsize=14, fontweight='bold')
#ax2.axis('off')

plt.tight_layout()  # Ajustar espaçamento
plt.show()

# === PASSO 5: RESULTADOS ===
print(f"\n=== RESULTADOS ===")
print(f"Componentes utilizados: {k}/{len(s)}")
print(f"Taxa de compressão: 50%")
print(f"Qualidade visual: Preservada com os componentes mais importantes")
