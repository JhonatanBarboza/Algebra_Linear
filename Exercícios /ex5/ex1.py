import numpy as np

def construir_operador_diagonalizavel():
    """
    Constrói a matriz de um operador linear diagonalizável T: R^3 -> R^3
    dados seus autovalores e autoespaços.
    """

    print("--- Construção do Operador Linear Diagonalizável ---")

    # 1. Definir os autovalores e os autovetores
    # Autovalor lambda = 2, autoespaço V(2) = span{(1, 2, 0), (0, 6, 1)}
    autovalor_1 = 2
    vetores_v2 = [np.array([1, 2, 0]), np.array([0, 6, 1])]

    # Autovalor lambda = 9, autoespaço V(9) = span{(1, 1, 1)}
    autovalor_2 = 9
    vetores_v9 = [np.array([1, 1, 1])]

    print(f"\nAutovalor 1 (λ1): {autovalor_1}")
    print(f"Autovetores para λ1: {vetores_v2[0]}, {vetores_v2[1]}")
    print(f"\nAutovalor 2 (λ2): {autovalor_2}")
    print(f"Autovetor para λ2: {vetores_v9[0]}")

    # 2. Construir a matriz D (diagonal de autovalores)
    # A ordem dos autovalores em D deve corresponder à ordem dos autovetores em P
    D = np.diag([autovalor_1, autovalor_1, autovalor_2])
    print("\nMatriz Diagonal D (autovalores):")
    print(D)

    # 3. Construir a matriz P (matriz dos autovetores como colunas)
    # Concatenamos os autovetores na ordem desejada para P
    # A ordem é (1,2,0), (0,6,1), (1,1,1) para corresponder a [2, 2, 9] em D
    P = np.column_stack([vetores_v2[0], vetores_v2[1], vetores_v9[0]])
    print("\nMatriz P (autovetores como colunas):")
    print(P)

    # 4. Calcular a inversa de P (P_inv)
    try:
        P_inv = np.linalg.inv(P)
        print("\nMatriz Inversa de P (P^-1):")
        # Arredondar para melhor visualização, pois pode haver pequenas imprecisões de ponto flutuante
        print(P_inv.round(decimals=4))
    except np.linalg.LinAlgError:
        print("\nErro: A matriz P não é invertível. Os autovetores podem não ser linearmente independentes.")
        return None

    # 5. Calcular a matriz do operador A = P @ D @ P_inv
    # O operador '@' realiza a multiplicação de matrizes no numpy
    A = P @ D @ P_inv
    print("\nMatriz do Operador Linear A (P @ D @ P^-1):")
    # Arredondar para lidar com pequenas imprecisões de ponto flutuante,
    # especialmente quando o resultado é exato como neste caso.
    print(A.round(decimals=4))

    return A

# Executar a função
if __name__ == "__main__":
    matriz_operador = construir_operador_diagonalizavel()
