def neural_network(input, weight):
    prediction = input * weight

    return prediction


weight = 0.1
alpha = 0.01

number_of_toes = [8.5]
win_or_lose_binary = [1]

input = number_of_toes[0]
goal_pred = win_or_lose_binary[0]

pred = neural_network(input, weight)

delta = pred - goal_pred
error = delta ** 2
weight_delta = delta * input
weight -= alpha * weight_delta #Если не будет коэфициента альфа, то будет слишком агрессивное изменение веса. Коэфициент помогает управлять скоростью обучения сети
