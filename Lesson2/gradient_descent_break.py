import matplotlib.pyplot as plt

weight, goal_pred, inp = (0.0, 0.8, 2.0)
# ------------ВИЗУАЛИЗАЦИЯ------------ #
X = []
Y = []
i = -11.2
while i <= 12.0:
    X.append(i)
    Y.append((inp * i - goal_pred) ** 2)
    i += 0.01
fig, ax = plt.subplots()
ax.plot(X, Y)
ax.plot([0.4] * len(Y), Y)
ax.grid()
ax.set_xlabel('Вес')
ax.set_ylabel('Ошибка')
# ------------------------------------ #
for iteration in range(20):
    pred = weight * inp
    error = (pred - goal_pred) ** 2
    if iteration < 4:  # ВИЗУАЛИЗАЦИЯ
        ax.scatter(weight, error, color="red")
        ax.text(weight, error + 20, str(iteration + 1))
    else:
        pass

    delta = (pred - goal_pred)
    weight_delta = delta * inp
    weight = weight - weight_delta
    print("Error: " + str(error) + " Prediction: " + str(pred))
    # Если посмотреть на вывод, то можно увидеть, что с каждой иттерацией ошибка увеличивается
    # А предсказание всё дальше и дальше от правильного ответа. Это происходит из-за большого входного
    # значения inp = 2. weigth_delta слишком чувствительна даже к маленькому изменению delta, поэтому
    # алгоритм рассходится.
plt.show()
