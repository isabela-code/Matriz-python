M = int(input("Quantidade de linhas da matriz : "))
N = int(input('Quantidade de colunas da matriz: '))
mat : [[int]] = [[0 for x in range(N)] for x in range(M)]
vet = [0 for x in range(M)]

for i in range(0, M):
    print(f"Digite os elementos da {i+1}a. linha")
    for j in range(0, N):
        mat[i][j] = int(input(f"Elemento [{i},{j}]: "))

print()
print("Vetor gerado : ")

for i in range (0,M):
    soma = 0 
    for j in range (0,N):
        soma = soma + mat[i][j]
    vet[i] = soma
for i in range (0,M):
    print(f'{vet[i]:.1f}')
