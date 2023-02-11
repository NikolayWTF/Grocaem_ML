# Задача. Вы попали в другой город и увидели незнакомый светофор. Нужно понять при какой
# комбинации сигналов можно переходить дорогу.
# В один момент может гореть несколько сигналов, всего на светофоре 3 сигнала
import numpy as np

streetlights = np.array([[1, 0, 1]])  # Для простоты демонстрации оставлю 1 набор входных данных
walk_vs_stop = np.array([0])

weights = np.array(
    [-0.5, 1.0, 0.5])  # Зададим 1 и 3 веса так, чтобы произведение их на соответствующие входы в сумме давало нуль
alpha = 0.1

error = 0

for iteration in range(10):
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

# Видим, что с первой же итерации мы получили нулевую ошибку, казалось бы, что это здорово
# Но по факту, если мы эту НС запустим на тестовом наборе данных, то она допустит много ошибок,
# НС не научилась понимать сути светофора, она лишь заучила набор входных данных
