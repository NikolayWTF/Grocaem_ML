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
alpha = 0.1 # При alpha = 1, алгоритм рассходится, а при alpha = 0.01 - сходится но медленно

for iteration in range(40):
    error_for_all_lights = 0
    for row_index in range(len(walk_vs_stop)):
        inp = streetlights[row_index]
        goal_prediction = walk_vs_stop[row_index]

        prediction = inp.dot(weights)

        error = (prediction - goal_prediction) ** 2
        delta = prediction - goal_prediction
        weights_delta = inp * delta
        weights -= alpha * weights_delta

        print("Prediction: " + str(prediction))
    print("Error: " + str(error) + "\n")