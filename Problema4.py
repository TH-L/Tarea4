#!/usr/bin/env python3
import numpy as np

### En este codigo se generara un arreglo de 10x10x10, que en un inicio tendra ceros
### Ahora se define el arreglo
a = np.zeros([10,10,10])
## Ahora se recorrera el arreglo en las tres posiciones (i,j,k) y si se cumplen tres condiciones se cambiara el valor de la posicon a 1
# 1. i es impar
# 2. j es par 
# 3. k es primo

### PAra abordar el problema vamos a definir una funcion que busque si un numero es primo

def primo(num):
    #Si desde un inicio el valor es menor o igual a 1 descartamos que sea primo
    if num <=1:
        return False
    # de igual modo si es 2 es primo.
    elif num ==2:
        return True
    else:
        # A partir de aqui probaremos dividir el numero entre los numeros desde 2 a num-1 
        # Si se encuentra otro divisor ya no es primo
        for i in range(2,num):
            ## Empleamos el operador modulo para encontrar divisores
            if num % i == 0:
                return False
        ### Una vez concluido el for si no se encontro divisor podemos asumir que se trata de un numero primo
        return True
    
### Una vez definida la funcion podemos hacer las evaluaciones de las posiciones en el array
### Usamos 3 for anidados

for i in range(10):
    for j in range(10):
        for k in range(10):
            if ((i % 2 != 0) and (j % 2 == 0) and (primo(k))):
                a[i, j, k]=1

print("Este es el arreglo modificado")
print(a)
print("\n")

print("Estas son celdas del arreglo modificado que deben ser 1:")
print(f'(1,0,2): {a[1,0,2]}')
print(f'(1,0,5): {a[1,0,5]}')
print(f'(1,0,7): {a[1,0,7]}')
print(f'(1,2,2): {a[1,2,2]}')

