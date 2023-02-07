# Функция получает два массива, поэлементно перемножает их значения и возвращает сумму всех полученных элементов
def w_sum(a, b):
    output = 0

    assert (len(a) == len(b)), "Длинны векторов не равны"

    for element in range(len(a)):
        output += (a[element] * b[element])

    return output


# Функция считает предсказание (pred)
def neural_network(function_inp, function_weights):
    function_prediction = w_sum(function_inp, function_weights)

    return function_prediction


# Умножнение числа (delta) на вектор (inp). Делаем остановку, обращение знака и масштабирование
def ele_mul(number, vector):
    output = [0, 0, 0]

    assert(len(output) == len(vector)), "Длинны векторов не равны"

    for ind in range(len(vector)):
        output[ind] = number * vector[ind]

    return output


weights = [0.1, 0.2, -0.1]

toes = [8.5, 9.5, 9.9, 9.0]  # Среднее число игр, сыгранных игроками
wlrec = [0.65, 0.8, 0.8, 0.9]  # Доля побед
nfans = [1.2, 1.3, 0.5, 1.0]  # Число болельщиков

win_or_lose_binary = [1, 1, 0, 1]

true = win_or_lose_binary[0]

inp = [toes[0], wlrec[0], nfans[0]]

prediction = neural_network(inp, weights)

error = (prediction - true) ** 2

delta = prediction - true

weights_deltas = ele_mul(delta, inp)

alpha = 0.01

for i in range(len(weights)):
    weights[i] -= alpha * weights_deltas[i]
print("Weights:" + str(weights))
print("Weights Deltas:" + str(weights_deltas))
