#!/usr/bin/env python3
import numpy as np

### En este codigo se generarn 20 calificaciones de un examen
### Se usa una semilla en especifico para que sea reproducible
### Se generan numeros que van del 0 al 100
generator = np.random.default_rng(1010)
data = np.round ( generator.uniform ( low = 0,
                    high = 101, # Se usa 101 para considerar el 100
                    size = 20 )
                 )
print("Estos son las calificaciones de 20 examenes")
print(data)
print("\n")

### Ahora se identificaran en el arrgelo las calificaciones que cumplan la condicion <60 que se replazaran con cero
### PAra ello empleamos el modulo de numpy where, este modulo regresa una tupla con los indices de los elementos que cumplen una condicion dada
menor_a_60 = np.where(data < 60)
print("Que posiciones sacaron menos de 60 puntos?")
print(menor_a_60)
print("\n")

### Sin embargo solo queremos cambiar los 3 primeros por lo que acortaremos el array para recuperar las posiciones 0,1 y 2 usando slicing
### Dado que el resultado de where es una tupla de un solo elemento incluimos un indice 0 antes de tomar los indices de 0 a 2 en el interior de la tupla
cambiar_a_0 = menor_a_60[0][:3] 
print("Estos cambiaran a 0")
print(cambiar_a_0)
print("\n")

### Realizamos la asignacion

data[cambiar_a_0]= 0
print("Estos son las calificaciones finales:")
print(data)
print("\n")