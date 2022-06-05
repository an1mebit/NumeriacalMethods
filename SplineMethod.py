import numpy as np
from math import sqrt
import matplotlib.pyplot as plt

def cubic_interp1d(x0, x, y):

    x = np.asfarray(x)
    y = np.asfarray(y)


    # Проверяем на то, отсортирован ли массив
    if np.any(np.diff(x) < 0):
        indexes = np.argsort(x)
        x = x[indexes]
        y = y[indexes]

    size = len(x)

    xdiff = np.diff(x)
    ydiff = np.diff(y)

    # Вводим буферные матрицы
    Li = np.empty(size)
    Li_1 = np.empty(size-1)
    z = np.empty(size)

    # Заполняем
    Li[0] = sqrt(2*xdiff[0])
    Li_1[0] = 0.0
    B0 = 0.0 # граница
    z[0] = B0 / Li[0]

    for i in range(1, size-1, 1):
        Li_1[i] = xdiff[i-1] / Li[i-1]
        Li[i] = sqrt(2*(xdiff[i-1]+xdiff[i]) - Li_1[i-1] * Li_1[i-1])
        Bi = 6*(ydiff[i]/xdiff[i] - ydiff[i-1]/xdiff[i-1])
        z[i] = (Bi - Li_1[i-1]*z[i-1])/Li[i]

    i = size - 1
    Li_1[i-1] = xdiff[-1] / Li[i-1]
    Li[i] = sqrt(2*xdiff[-1] - Li_1[i-1] * Li_1[i-1])
    Bi = 0.0
    z[i] = (Bi - Li_1[i-1]*z[i-1])/Li[i]

    # Решаем уравнение
    i = size-1
    z[i] = z[i] / Li[i]
    for i in range(size-2, -1, -1):
        z[i] = (z[i] - Li_1[i-1]*z[i+1])/Li[i]

    # Ищем индекс из массива для формулы сплайнов
    index = x.searchsorted(x0)
    np.clip(index, 1, size-1, index)

    xi1, xi0 = x[index], x[index-1]
    yi1, yi0 = y[index], y[index-1]
    zi1, zi0 = z[index], z[index-1]
    hi1 = xi1 - xi0

    # Вычисляем сплайн
    f0 = zi0/(6*hi1)*(xi1-x0)**3 + \
         zi1/(6*hi1)*(x0-xi0)**3 + \
         (yi1/hi1 - zi1*hi1/6)*(x0-xi0) + \
         (yi0/hi1 - zi0*hi1/6)*(xi1-x0)
    print(f0)
    return f0

if __name__ == '__main__':
    x = np.array([-4,-3,-2,-1,0,1,2,3,4])
    y = np.array([-3.02721,0.42336,1.81859,0.84147,0,0.84147,1.81859,0.42336,-3.02721])
    plt.scatter(x, y)

    x_new = np.linspace(-4,4,200) #эта штука создаёт массив с шагом 200
    plt.plot(x_new, cubic_interp1d(x_new, x, y))

    plt.show()