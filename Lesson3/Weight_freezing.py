#Попытаюсь обучить сеть, используя только два веса (второй и третий). Первый вес будет заморожен
# Функция считает предсказание (pred)
def neural_network(function_inp, function_weights):
    out = 0
    for element in range(len(function_inp)):
        out += (function_inp[element] * function_weights[element])
    return out

# Умножнение числа (delta) на вектор (inp). Делаем остановку, обращение знака и масштабирование
def ele_mul(number, vector):
    output = [0, 0, 0]

    assert(len(output) == len(vector)), "Длинны векторов не равны"

    for ind in range(len(vector)):
        output[ind] = number * vector[ind]

    return output

toes = [8.5, 9.5, 9.9, 9.0]  # Среднее число игр, сыгранных игроками
wlrec = [0.65, 0.8, 0.8, 0.9]  # Доля побед
nfans = [1.2, 1.3, 0.5, 1.0]  # Число болельщиков

win_or_lose_binary = [1, 1, 0, 1]
true = win_or_lose_binary[0]

alpha = 0.3
weights = [0.1, 0.2, -0.1]
inp = [toes[0], wlrec[0], nfans[0]]

for iteration in range(3):
    prediction = neural_network(inp, weights)

    error = (prediction - true) ** 2
    delta = prediction - true

    weights_deltas = ele_mul(delta, inp)
    weights_deltas[0] = 0 # Замораживаю первый вес

    print("Iteration:", iteration + 1)
    print("Pred:", prediction)
    print("Error:", error)
    print("Delta:", delta)
    print("Weights:", weights)
    print("Weight_Deltas:", weights_deltas, "\n")

    for i in range(len(weights)):
        weights[i] -= alpha * weights_deltas[i]

# Видим, что схождение достигнуто. Это значит, что последующая попытка выполнить обучение первого веса
# Ничего не даст. То-есть если сеть случайно выяснит, как получить точный прогноз на обучающей
# выборке, без участия того или иного веса, то она не научится включать его в прогноз.