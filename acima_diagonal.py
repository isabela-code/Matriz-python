M = int(input("Qual a ordem da matriz : "))
mat : [[int]] = [[0 for x in range(M)] for x in range(M)]
soma = 0 

for i in range(0, M):
    for j in range(0, M):
        mat[i][j] = int(input(f"Elemento [{i},{j}]: "))
print()
for i in range(0, M):
    for j in range(0, M):
        if j > i:
            soma = soma + mat[i][j]
print(f'Soma dos elementos acima da diagonal principal : {soma} ')