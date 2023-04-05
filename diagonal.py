M = int(input("Qual a ordem da matriz : "))
mat : [[int]] = [[0 for x in range(M)] for x in range(M)]
negativo = 0 

for i in range(0, M):
    for j in range(0, M):
        mat[i][j] = int(input(f"Elemento [{i},{j}]: "))

print()
print("Diagonal principal : ")

for i in range (0,M):
    for j in range (0,M):
       if i == j:
           print(f"{mat[i][j]} ", end='')
print()
for i in range (0,M):
    for j in range (0,M):
        if mat[i][j] < 0 :
            negativo = negativo + 1
print(f'Quantidade de negativos = {negativo}')