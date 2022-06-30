import os
import numpy as np
from matplotlib import pyplot
from scipy import optimize
from scipy.io import loadmat

import utils


def predict(theta_1, theta_2, x):
    """
    Predict the label of an input given a trained neural network.

    Parameters
    ----------
    theta_1 : array_like
        Weights for the first layer in the neural network.
        It has shape (2nd hidden layer size x input size)

    theta_2: array_like
        Weights for the second layer in the neural network.
        It has shape (output layer size x 2nd hidden layer size)

    x : array_like
        The image inputs having shape (number of examples x image dimensions).

    Return
    ------
    p : array_like
        Predictions vector containing the predicted label for each example.
        It has a length equal to the number of examples.

    Hint
    ----
    This code can be done all vectorized using the numpy argmax function.
    In particular, the argmax function returns the index of the  max element,
    for more information see '?np.argmax' or search online. If your examples
    are in rows, then, you can use np.argmax(A, axis=1) to obtain the index
    of the max for each row.

    """
    # Asegurar que la entrada tenga dos dimensiones
    if x.ndim == 1:
        x = x[None]  # promover a dos dimensiones

    # Variables útiles
    m = x.shape[0]
    num_labels = theta_2.shape[0]

    p = np.zeros(x.shape[0])

    x = np.concatenate([np.ones((m, 1)), x], axis=1)

    a2 = utils.sigmoid(x.dot(theta_1.T))
    a2 = np.concatenate([np.ones((a2.shape[0], 1)), a2], axis=1)

    p = np.argmax(utils.sigmoid(a2.dot(theta_2.T)), axis=1)

    return p


def run():
    data = loadmat('ex3data1.mat')
    x, y = data['X'], data['y'].ravel()

    # Se convierte la etiqueta 10 a 0
    y[y == 10] = 0

    m = y.size

    # se permutan los ejemplos, para ser usados para visualizar ina imagen a la vez
    indices = np.random.permutation(m)

    # Selecciona 100 puntos al azar de datos para visualizar
    rand_indices = np.random.choice(m, 100, replace=False)
    sel = x[rand_indices, :]
    # sel = x[0,:]
    utils.displayData(sel)

    # Configura los parámetros que se requieren
    input_layer_size = 400  # Entrada Imagen de Digitos de 20x20
    hidden_layer_size = 25  # 25 unidades ocultas
    num_labels = 10  # 10 etiquetas, del 1 al 10 (se remapea el numero 10 con el valor de 0)

    # Carga el archivo .mat, que devuelve un diccionario
    weights = loadmat('ex3weights.mat')

    # Obtiene el modelo de pesos del diccionario
    # theta_1 has size 25 x 401
    # theta_2 has size 10 x 26
    theta_1, theta_2 = weights['Theta1'], weights['Theta2']

    # intercambia la primera y la última columna de theta_2, debido al legado de la indexación de MATLAB,
    # desde que el archivo de peso ex3weights.mat se guardó según la indexación de MATLAB
    theta_2 = np.roll(theta_2, 1, axis=0)

    pred = predict(theta_1, theta_2, x)
    print('Precisión del conjunto de entrenamiento: {:.1f}%'.format(np.mean(pred == y) * 100))
    pyplot.show()


run()