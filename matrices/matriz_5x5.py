matriz=[]
for i in range(5):
    fila=[]
    for j in range(5):
        numero=int(input(f"Ingrese el numero para la posicion [{i}][{j}]: "))
        fila.append(numero)
    matriz.append(fila)     
print("La matriz ingresada es:")
for i in range(5):
    for j in range(5):
        print(matriz[i][j], end=" ")
    print()  