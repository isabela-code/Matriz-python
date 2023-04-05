M = int(input("Qual a ordem da matriz : "))
mat : [[int]] = [[0 for x in range(M)] for x in range(M)]
vet = [0 for x in range (M)]

for i in range(0, M):
    for j in range(0, M):
        mat[i][j] = int(input(f"Elemento [{i},{j}]: "))

print()
print("Maior elemento de cada linha : ")

for i in range (0,M):
    maior = mat[0][0]
    for j in range (0,M):
        if mat[i][j] > maior:
            maior = mat[i][j]
            vet[i] = maior 
for i in range(M):
	print(f"{vet[i]:.1f}")