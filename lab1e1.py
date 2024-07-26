import numpy as np
import matplotlib.pyplot as plt

def graficar_campo_direcciones(f, xmin, xmax, ymin, ymax, xstep, ystep, normalizar=False, mostrar_flujo=False):
    # Crear rangos y subdivisiones en los ejes x e y
    x = np.linspace(xmin, xmax, xstep)
    y = np.linspace(ymin, ymax, ystep)

    # Generar la rejilla de puntos a graficar
    X, Y = np.meshgrid(x, y)

    # Evaluar la función f en cada punto de la rejilla
    U, V = np.zeros(X.shape), np.zeros(Y.shape)
    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            U[i, j], V[i, j] = f(X[i, j], Y[i, j])

    # Si se desea graficar el campo unitario
    if normalizar:
        magnitud = np.hypot(U, V)
        U, V = U / magnitud, V / magnitud

    # Graficar el campo vectorial usando quiver
    plt.figure(figsize=(10, 7))
    plt.quiver(X, Y, U, V, color='green', scale=10, width=0.003)
    plt.title('Campo de Direcciones')
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.grid()

    # Graficar las líneas de flujo si se especifica
    if mostrar_flujo:
        plt.streamplot(X, Y, U, V, color='orange', linewidth=1, density=2)

    plt.show()

def F1(x, y):
    dx = -y
    dy = x - np.cos(x)
    return dx, dy
def F2(x, y):
    dx = np.sin(x) - y
    dy = x + np.cos(y)
    return dx, dy


# Ejemplo de uso
graficar_campo_direcciones(F2, xmin=-3, xmax=3, ymin=-2, ymax=2, xstep=20, ystep=20, normalizar=False, mostrar_flujo=True)
