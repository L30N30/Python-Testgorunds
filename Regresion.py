import os
import numpy as np
from matplotlib import pyplot


def graficar_datos(x, y):
  fig = pyplot.figure()
  pyplot.plot(x, y, 'ro')
  pyplot.xlabel('Grado de acides del cafe')
  pyplot.ylabel('Nivel de tintura del cafe')


data = np.loadtxt('ejemplo01.txt', delimiter=',')
X, y = data[:, 0], data[:,1]
m = y.size