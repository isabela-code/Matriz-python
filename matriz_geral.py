import math

M = int(input("Qual a ordem da matriz : "))
mat = [[0 for x in range(M)] for x in range(M)]
soma = 0 
vet =[0 for x in range(M)]
vet1 = [0 for x in range(M)]
vet2 = [0 for x in range(M)]

for i in range(0, M):
    for j in range(0, M):
        mat[i][j] = int(input(f"Elemento [{i},{j}]: "))
print()
for i in range(0, M):
    for j in range(0, M):
        if mat[i][j] > 0:
            soma = soma + mat[i][j]
print(f'Soma dos positivos = {soma}')
print()
y = int(input('Escolha uma linha: '))
print('Linha escolhida : ', end='')
for i in range(M):
        print(f'{mat[y][i]:.1f} ', end='')
print()
y = int(input('Escolha uma coluna: '))
print('Coluna escolhida : ', end='')
for i in range(M):
    print(f'{mat[i][y]:.1f} ', end='')
print()
print('Diagonal principal:', end='')
for i in range(M):
    print(f'{mat[i][i]: .1f} ',end='')
print()
for i in range(M):
    for j in range(M):
        if mat[i][j] < 0:
            mat[i][j]= math.pow(mat[i][j],2);
print('Matriz alterada: ')
for i in range(M):
    for j in range(M):
        print(f'{mat[i][j]:.1f} ', end='')
    print()
