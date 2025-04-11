#!/usr/bin/env python3
import numpy as np

### En este codigo se generara un arreglo de 10x10x10, que en un inicio tendra ceros
### Ahora se define el arreglo
a = np.zeros([10,10,10])
## Ahora se recorrera el arreglo en las tres posiciones (i,j,k) y si se cumplen tres condiciones se cambiara el valor de la posicon a 1
# 1. i es impar
# 2. j es par 
# 3. k es primo

### Para abordar el problema vamos a definir una funcion que busque los numero primos dentro de un rango

def obtener_primos(size):
    ### definimos un set para almacenar los numeros primos encontrados
    primos = []
    for num in range(size):
        # En un inicio asumimos que el numero es primo 
        es_primo=True
        #Si desde un inicio el valor es menor o igual a 1 descartamos que sea primo
        if num <=1:
            es_primo=False
        # de igual modo si es 2 es primo.
        elif num ==2:
            es_primo=True
        else:
            # A partir de aqui probaremos dividir el numero entre los numeros desde 2 a num-1 
            # Si se encuentra otro divisor ya no es primo
            for i in range(2,num):
                ## Empleamos el operador modulo para encontrar divisores
                if num % i == 0:
                    es_primo=False
                    # Si se encontro otro divisor se detiene el for, no hace falta buscar mas
                    break
            ### Una vez concluido el for si no se encontro divisor podemos asumir que se trata de un numero primo
        if es_primo:
            primos.append(num)
    return primos
            
### Obtenemos los numeros primos hasta el 10, rango de nuestro arreglo  
primos = obtener_primos(10)

### se evalua cada condicion
impar =(np.arange(10) % 2 == 1).reshape(-1,1,1)
par =(np.arange(10) % 2 == 0).reshape(1,-1,1)
primo = np.isin(np.arange(10), primos).reshape(1, 1, -1)

### Se genera la mascara en la cual se cumplen las tres condiciones
mask = impar & par & primo

### Se modifica el arreglo con esta mascara
a[mask] = 1


print("Este es el arreglo modificado")
print(a)
print("\n")

print("Estas son celdas del arreglo modificado que deben ser 1:")
print(f'(1,0,2): {a[1,0,2]}')
print(f'(1,0,5): {a[1,0,5]}')
print(f'(1,0,7): {a[1,0,7]}')
print(f'(1,2,2): {a[1,2,2]}')


