#!/usr/bin/env python3
import numpy as np

### En este codigo se generaran 10 peces con su tamano
### Un arreglo 3D de 5x5x5
### Los peces se moveran a manera que el pez mas grande en un espacio se comera al pequeno y ocupara la celda
### Al final de los movimientos se obtiene que peces sobreviven

### Se define este arreglo 2D que indica como se moveran los peces
locs = np.array([
    [0, 0, 0],
    [1, 1, 2],
    [0, 0, 0],
    [2, 1, 3],
    [5, 5, 4],
    [5, 0, 0],
    [5, 0, 0],
    [0, 0, 0],
    [2, 1, 3],
    [1, 3, 1]
])

### Se generan los peces con peso_actuals aleatorios. Y se usa una semilla para la reproducibilidad de los datos
generator = np.random.default_rng(1010)
weights = generator.normal(size=10)
print("Estos son los pesosde los peces")
print(weights)
print("\n")

### Ahora se define el tanque de agua donde se moveran los peces
## En un incio solo tendra ceros indicando que esta vacio
tanque = np.zeros([6,6,6])

### Se empiezan a mover los peces en el tanque
### Se define un conjunto  en la que se almacenaran los indices de los peces que vayan muriendo, en un inicio se encuentra vacio

muertos=set()
for i in range(len(locs)):
    ## Definimos la posicion final a la que se movera el pez
    pos=locs[i]
    ## Definimos el peso del pez que se esta moviendo
    peso_actual=weights[i]
    ## Definimos el peso del pez que ya se encuentra en el tanque, sera cero si la poscion esta vacia
    peso_pos =tanque[pos[0], pos[1], pos[2]]
    
    # Verificamos si el pez salio de rango, en cuyo caso estaria muerto por salir del agua
    if (pos[0] > 4 or pos[1] > 4 or pos[2] >4):
        muertos.add(peso_actual)
    
    # Ahora verificamos si la posicion a desplazarse en el tanque esta vacia
    if peso_pos == 0:
        ### Si esta vacia asignamos el peso_actual del pez a esa celda del tanque
        tanque[pos[0], pos[1], pos[2]] = peso_actual
    else:
        ### si la celda ya esta ocupada se comparan el peso_actual y el peso_pos de los peces
        ### Si el peso_actual del pez actual es mayor al que ya estaba en la celda, peso_pos, el pez que estaba ahi morira
        if peso_actual > peso_pos:
            ### El peso_pos del pez que estaba en dicha posicion se agregara al conjunto de peces muertos
            muertos.add(peso_pos)
            ### el pez actual ocupara su lugar en el tanque
            tanque[pos[0], pos[1], pos[2]] = peso_actual
        else:
            ### Si el pez que ya se encontraba en la celda es mayor o igual se comera al nuevo pez, 
            ### Mantendra su posicion y el pez actual se agrega al conjunto de pesos muertos
            muertos.add(peso_actual)
            
### Una vez que se haya concluido con el desplazamiento de los peces se obtienen los peces que no esten el set muertos,
### Es decir los que sobrevivieron:
sobrevivientes = sobrevivientes = [i for i in range(len(weights)) if weights[i] not in muertos]

print("Estos peces sobrevivieron:")
print(sobrevivientes)

