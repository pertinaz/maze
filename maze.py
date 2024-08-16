import random
import numpy as np
import matplotlib.pyplot as plt


# Dimensiones del laberinto

rows, cols = 10, 10

# Direcciones posibles (arriba, abajo, izquierda, derecha)
directions = [(0,1),(1,0),(0,-1),(-1,0)]

# depth first search para generar el laberinto
def generate_maze(grid,row,col):
    grid[row,col] = 1
    random.shuffle(directions) # se genera direccion de movimiento aleatorio

    for direction in directions:
        new_row, new_col = row + direction[0], col + direction[1]
        between_row, between_col = row + direction[0] // 2, col + direction[1] // 2

        if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row, new_col] == 0:
            grid[between_row, between_col] = 1
            generate_maze(grid,new_row,new_col)

# cuadricula

grid = np.zeros((rows * 2 - 1, cols * 2 - 1),dtype=int)

# hacer que el laberinto se genere desde la esquina superior izquierda
generate_maze(grid,0,0)

# dibujar el laberinto

plt.figure(figsize=(10,10))
plt.imshow(grid,cmap='binary')
plt.xticks([]) # Eliminar marcas de eje x
plt.yticks([])  # Eliminar marcas de eje y
plt.show()