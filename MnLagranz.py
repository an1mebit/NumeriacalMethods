import numpy as np

x_Row=np.array([...], dtype=float)
y_Row=np.array([...], dtype=float)

def Lagranz(x_Row, y_Row, x):
    z=0
    for j in range(len(y_Row)):
        p1 = 1; p2 = 1
        for i in range(len(x_Row)):
            if i==j:
                p1=p1*1; p2=p2*1
            else:
                p1=p1*(x-x_Row[i])
                p2=p2*(x_Row[j]-x_Row[i])
        z=z+y_Row[j]*p1/p2
    return z