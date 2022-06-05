import numpy as np

x_Row=np.array([...], dtype=float)
y_Row=np.array([...], dtype=float)

def kvadr_aprocsimation(x_Row, y_Row):
    x1 = []; x2 = []; x3 = []; x4 = []
    y = []; xy = []; x2y = []
    
    for i in range(len(x_Row)):
        x1.append(x_Row[i])
        x2.append(x_Row[i]**2)
        x3.append(x_Row[i]**3)
        x4.append(x_Row[i]**4)
        y.append(y_Row[i])
        xy.append(x_Row[i]*y_Row[i])
        x2y.append((x_Row[i]**2) * y_Row[i])

    left_arr = np.array([[sum(x4),sum(x3),sum(x2)],[sum(x3),sum(x2),sum(x1)],[sum(x2),sum(x1),len(x_Row)]])
    right_arr = np.array([sum(x2y),sum(xy),sum(y)])

    coef = np.linalg.solve(left_arr,right_arr)
    
    F = []

    for i in range(len(x_Row)):
        F.append(coef[0]*x_Row[i]**2+coef[1]*x_Row[i]+coef[2])

    return F

def liner_aprocsimation(x_Row, y_Row):
    x1 = []; x2 = []; xy = []; y = []

    for i in range(len(x_Row)):
        x1.append(x_Row[i])
        x2.append(x_Row[i]**2)
        y.append(y_Row[i])
        xy.append(x_Row[i]*y_Row[i])

    left_arr = np.array([[sum(x2), sum(x1)],[sum(x1),len(x_Row)]])
    right_arr = np.array([sum(xy),sum(y)])

    coef = np.linalg.solve(left_arr,right_arr)

    print(coef)

    F = []

    for i in range(len(x_Row)):
        F.append(coef[0]*x_Row[i] + coef[1])
    
    return F