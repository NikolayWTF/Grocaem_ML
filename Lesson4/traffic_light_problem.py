# Задача. Вы попали в другой город и увидели незнакомый светофор. Нужно понять при какой
# комбинации сигналов можно переходить дорогу.
# В один момент может гореть несколько сигналов, всего на светофоре 3 сигнала
import numpy as np

streetlights = np.array([[1, 0, 1],
                         [0, 1, 1],
                         [0, 0, 1],
                         [1, 1, 1],
                         [0, 1, 1],
                         [1, 0, 1]])
walk_vs_stop = np.array([0, 1, 0, 1, 1, 0])

weights = np.array([1.0, 1.0, 1.0])
alpha = 0.1 # При alpha = 1, алгоритм рассходится

inp = streetlights[0]
goal_prediction = walk_vs_stop[0]

for iteration in range(20):
    prediction = inp.dot(weights)
    error = (goal_prediction - prediction) ** 2
    delta = prediction - goal_prediction
    weights_delta = inp * delta
    weights -= alpha * weights_delta

    print("Error: " + str(error) + " Prediction: " + str(prediction))