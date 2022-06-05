import numpy as np

x_Row=np.array([...], dtype=float)
y_Row=np.array([...], dtype=float)

def table(x_Row, y_Row):
    """
         Получить таблицу интерполяции Ньютона
         : param x_Row: значение списка x
         : param y_Row: значение списка y
         : return: вернуть таблицу интерполяции
    """
    quotient = [[0] * len(x_Row) for _ in range(len(x_Row))]

    for n_ in range(len(x_Row)):
        quotient[n_][0] = y_Row[n_]
    for i in range(1, len(x_Row)):
        for j in range(i, len(x_Row)):
            # j-i определяет диагональные элементы
            quotient[j][i] = (quotient[j][i - 1] - quotient[j - 1][i - 1]) / (x_Row[j] - x_Row[j - i])
    return quotient

def get_corner(result):
    """
         Получить диагональные элементы через таблицу интерполяции
         : param result: результат таблицы интерполяции
         : return: диагональный элемент
    """
    link = []
    
    for i in range(len(result)):
        link.append(result[i][i])
    return link

def newton(corner_Row, x_Row, x):
    """
         Результат интерполяции Ньютона
         : param corner_Row: диагональ решаемой задачи
         : param x: входное значение
         : param x_Row: исходное значение списка x
         : return: результат интерполяции Ньютона
    """
    result = corner_Row[0]

    for i in range(1, len(corner_Row)):
        p = corner_Row[i]
        for j in range(i):
            p *= (x - x_Row[j])
        result += p
    return result

x=0.5
#Пример вывода
print(newton(get_corner(table(x_Row,y_Row)),x_Row,x))
