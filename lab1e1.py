import numpy as np
import matplotlib.pyplot as plt

def graficar_campo_direcciones(f, xmin, xmax, ymin, ymax, xstep, ystep, normalizar=False, mostrar_flujo=False):
    x = np.linspace(xmin, xmax, xstep)
    y = np.linspace(ymin, ymax, ystep)
    X, Y = np.meshgrid(x, y)

    A, B = np.zeros(X.shape), np.zeros(Y.shape)
    
    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            A[i, j], B[i, j] = f(X[i, j], Y[i, j])

    if normalizar:
        magnitud = np.hypot(A, B)
        A, B = A / magnitud, B / magnitud
        
    plt.figure(figsize=(10, 7))
    plt.quiver(X, Y, A, B, color='green', scale=10, width=0.003)
    plt.title('Campo de Direcciones')
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.grid()

    if mostrar_flujo:
        plt.streamplot(X, Y, A, B, color='orange', linewidth=1, density=2)
    
    plt.show()

def F1(x, y):
    dx = -y
    dy = x - np.cos(x)
    return dx, dy

def F2(x, y):
    dx = np.sin(x) - y
    dy = x + np.cos(y)
    return dx, dy

def F3(x, y):
    dx = 2*x-y+3*(x**2-y**2)+2*x*y
    dy = x-3*y-3*(x**2-y**2)+2*x*y
    return dx, dy

# Ejemplo de uso
graficar_campo_direcciones(F2, xmin=-3, xmax=3, ymin=-2, ymax=2, xstep=20, ystep=20, normalizar=False, mostrar_flujo=True)
# Ejemplo de uso
graficar_campo_direcciones(F3, xmin=-3, xmax=3, ymin=-2, ymax=2, xstep=20, ystep=20, normalizar=True, mostrar_flujo=False)
