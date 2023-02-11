weight, goal_pred, input = (0.0, 0.8, 0.5)

for iteration in range(20):

    pred = input * weight
    #Поменяю pred на формулу по которой он вычисляется
    error = (input * weight - goal_pred) ** 2 #Так как input и goal_pred = const, то из этой строчки видна зависимость ошибки от веса
    #Нам нужно изменить вес так, чтобы сместить ошибку к нулю. График зависимости ошибки от веса будет иметь форму параболы
    #Угол наклона касательной, проведённый к точке (error, weight) - будет указывать направление к вершине параболы
    #А тангенс угла наклона касательной к точке - это производная
    delta = pred - goal_pred
    weight_delta = delta * input
    weight -= weight_delta
    print("Error: " + str(error) + " Prediction: " + str(pred))
