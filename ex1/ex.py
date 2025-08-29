import sympy as sp

# Matrizes geradoras
A1 = sp.Matrix([[0,0],[1,1],[0,0]])
A2 = sp.Matrix([[0,1],[0,-1],[1,0]])
A3 = sp.Matrix([[0,1],[0,0],[0,0]])

# Matriz que queremos verificar
A  = sp.Matrix([[0,2],[3,4],[5,0]])

# Função para transformar matriz 3x2 em vetor coluna (6x1)
def to_vector(M):
    return sp.Matrix(M).reshape(6,1)

# Vetores correspondentes
v1, v2, v3, v = map(to_vector, [A1, A2, A3, A])

# Monta a matriz do sistema [v1 v2 v3]
M = sp.Matrix.hstack(v1, v2, v3)

# Tenta resolver sistema linear M * [α β γ]^T = v
try:
    sol = M.gauss_jordan_solve(v)
    print("A matriz A PERTENCE ao subespaço W.")
    print("Coeficientes encontrados (α, β, γ):", sol)

except ValueError:
    print("A matriz A NÃO pertence ao subespaço W.")
