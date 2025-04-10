#!/usr/bin/env python3
import numpy as np

### En este codigo se generarn 10 puntajes del amr aleatorios
### Se usa una semilla en especifico para que sea reproducible
### Se generan numeros que van del 0 al 100
generator = np.random.default_rng(1010)
data = np.round ( generator.uniform ( low = 0,
                    high = 101, # Se usa 101 para considerar el 100
                    size = 10 )
                 )
print("Estos son los puntajes del amor de 10 personas")
print(data)
print("\n")

### Ahora lo que se quiere hacer es comparar las diferencias entre los puntajes de 
### las 10 personas, estos datos se almacenaran en una matriz de numpy de 2 dimensiones.

### Se crea una matriz de diferencias de 10 x 10
## En un incio solo tendra ceros
matrix_diff= np.zeros([10,10])

### Se prueban dos metodos, el primero usando for
##Ahora se recorrera la matriz tanto en i como en j y se obtendra una resta de los puntajes
for i in range(10):
   for j in range(10):
      matrix_diff[i,j] = abs(data[i] - data[j])

print("Esta es la matriz generada usando for:")
print(matrix_diff)
print("\n")

### El segundo metodo a probar es haciendo uso de operaciones vectoriales de numpy
### a traves del metodo newaxis
print("Asi se transformo data a columnas usando newaxis:")
print(data[:, np.newaxis])
print("\n")
### En este caso podemos hacer solo una linea de codigo que genere la matriz de diferencias

diff_matrix = np.abs(data[:, np.newaxis] - data)
### Se calculan las diferencias entre data ahora convertida como columnas y cada valor dentro de data
print("Esta es la matriz generada usando newaxis:")
print(matrix_diff)
print("\n")
