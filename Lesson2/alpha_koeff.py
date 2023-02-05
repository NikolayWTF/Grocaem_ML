# Для того, чтобы бороться с избыточной коррекцией можно использовать альфа коэффициент - число
# в диапозоне от 0 до 1
# Теперь будем вычислять weigth следующим образом: weigth = weigth - weigth_delta * alpha_koefficient

weight, goal_pred, input = (0.0, 0.8, 2.0)
alpha = 0.2

for i in range(20):

    pred = input*weight
    error = (pred - goal_pred) ** 2
    delta = pred - goal_pred
    weight_delta = input * delta
    weight = weight - weight_delta * alpha
    print("Error: " + str(error) + " Prediction: " + str(pred))