M = int(input("Quantas linhas a matriz tera : "))
N = int(input('Quantas colunas a matriz tera: '))
mat1 : [[int]] = [[0 for x in range(N)] for x in range(M)]
mat2 : [[int]] = [[0 for x in range(N)] for x in range(M)]
vet1 = [0 for x in range(N)]
vet2 = [0 for x in range(N)]
vet3 = [0 for x in range(N)]
vet4 = [0 for x in range(N)]
vets1 = [0 for x in range (N)]
vets2 = [0 for x in range(N)]

print('Digite os valores da matriz A:')
for i in range(0, M):
    for j in range(0, N):
        mat1[i][j] = int(input(f"Elemento [{i},{j}]: "))
print('Digite os valores da matriz B:')
for i in range(0, M):
    for j in range(0, N):
        mat2[i][j] = int(input(f"Elemento [{i},{j}]: "))

print()
print("Matriz soma : ")

for i in range (0,M-1):
    for j in range (0,N):
        vet1[j]= mat1[i][j]
for i in range (0,M-1):
    for j in range (0,N):
        vet2[j]= mat2[i][j]
for i in range (1,M):
    for j in range (0,N):
        vet3[j]= mat1[i][j]
for i in range (1,M):
    for j in range (0,N):
        vet4[j]= mat2[i][j]
for j in range(0,N):
    vets1[j] = vet1[j] + vet2[j]
for j in range(0,N):
    vets2[j] = vet3[j] + vet4[j]
for j in range(0,N):
    print(f'{vets1[j]} ',end='')
print()
for j in range(0,N):
    print(f'{vets2[j]} ',end='')

    

        
        