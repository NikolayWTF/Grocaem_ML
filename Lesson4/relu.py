# Не всегда есть явная корреляция между входом и выходом. Предположим, что переходить
# дорогу можно, если горит 1 и 3 сигналы, или 2 и 3. В таком случае нет прямой корреляции
# между входным узлом и выходным. Поэтому сделаем искусственную корреляцию. Нужно, чтобы
# входные узлы генерировали набор данных, который будет коррелировать с выходным слоем,
# для этого добавим ещё один слой в НС
# ОДНАКО !!! Для любой трёхслойной сети, существует двухслойная сеть с идентичным поведением!!!
# Это легко понять на примере умножения. Любое равенство с тремя сомножителями,
# можно представить в виде равенства с двумя сомножителями. Поэтому нам необходимо в какой-то момент
# изменить значение того или иного узла. В этом нам поможет функция активации relu
# Если значение узла в скрытом слое, падает ниже нуля, тогда relu делает его нулевым. Таким образом
# узел потеряет корреляцию с входным узлом и сможет получить корреляцию с другим узлом.

import numpy as np

np.random.seed(1)


def relu(x):
    return (x > 0) * x  # Если True, то 1 * х, если False, то 0 * х


def relu2deriv(output):
    return output > 0


alpha = 0.2
hidden_size = 4  # Размерность скрытого слоя

streetlights = np.array([[1, 0, 1],
                         [0, 1, 1],
                         [0, 0, 1],
                         [1, 1, 1]])

walk_vs_stop = np.array([[1, 1, 0, 0]]).T

weights_0_1 = 2 * np.random.random((3, hidden_size)) - 1
weights_1_2 = 2 * np.random.random((hidden_size, 1)) - 1

for iteration in range(60):
    layer_2_error = 0
    for i in range(len(streetlights)):
        layer_0 = streetlights[i:i+1]
        layer_1 = relu(np.dot(layer_0, weights_0_1))
        layer_2 = np.dot(layer_1, weights_1_2)

        layer_2_error += np.sum((layer_2 - walk_vs_stop[i:i+1]) ** 2)

        layer_2_delta = (walk_vs_stop[i:i+1] - layer_2)
        layer_1_delta = layer_2_delta.dot(weights_1_2.T)* relu2deriv(layer_1)

        weights_1_2 += alpha * layer_1.T.dot(layer_2_delta)
        weights_0_1 += alpha * layer_0.T.dot(layer_1_delta)

    if(iteration % 10 == 9):
        print("Error:" + str(layer_2_error))
