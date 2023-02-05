weight, goal_pred, input = (0.0, 0.8, 2.0)

for iteration in range(20):
    pred = weight * input
    error = (pred - goal_pred) ** 2
    delta = (pred - goal_pred)
    weight_delta = delta*input
    weight = weight - weight_delta
    print("Error: " + str(error) + " Prediction: " + str(pred))
    # Если посмотреть на вывод, то можно увидеть, что с каждой иттерацией ошибка увеличивается
    # А предсказание всё дальше и дальше от правильного ответа. Это происходит из-за большого входного
    # значения input = 2. weigth_delta слишком чувствительна даже к маленькому изменению delta, поэтому
    # производная рассходится.