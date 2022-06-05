import math
import numpy as np

#Задаём функцию, которую мы должны проинтегрировать
def fn1(x):
    return math.log(math.sqrt(x**2+1))

def fn2(x):
    return math.sqrt(x**2+1)*math.cos(x**2)

#Метод трапеций
def tr_integral(f,xmin,xmax,n):
    h=(xmax-xmin)/n
    area=0
    x=xmin
    for i in range(n):
        area+=h*(f(x)+f(x+h))/2
        x+=h
    return area

#Метод прямоугольников
def rect_integral(f,xmin,xmax,n):
    h=(xmax-xmin)/n
    area=0
    x=xmin
    for i in range(n):
        area+=h*f(x)
        x+=h
    return area

print(tr_integral(fn1, 0,1,5))
print(rect_integral(fn2,0,1,5))