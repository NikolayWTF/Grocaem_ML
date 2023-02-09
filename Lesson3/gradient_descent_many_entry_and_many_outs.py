# Функция получает два массива, поэлементно перемножает их значения и возвращает сумму всех полученных элементов
def w_sum(a, b):
    output = 0

    assert (len(a) == len(b)), "Длинны векторов не равны"

    for element in range(len(a)):
        output += (a[element] * b[element])

    return output


def vect_mat_mul(vect, matrix):
    output = [0, 0, 0]

    assert (len(vect) == len(matrix))

    for i in range(len(vect)):
        output[i] = w_sum(vect, matrix[i])

    return output


def neural_network(input, weights):
    pred = vect_mat_mul(input, weights)

    return pred


def zeros_matrix(len_a, len_b):
    matrix = []
    for i in range(len_a):
        second_matrix = []
        for j in range(len_b):
            second_matrix.append(0)
        matrix.append(second_matrix)
    return matrix


def outer_prod(vec_a, vec_b):
    out = zeros_matrix(len(vec_a), len(vec_b))

    for i in range(len(vec_a)):
        for j in range(len(vec_b)):
            out[i][j] = vec_a[i] * vec_b[j]
    return out


#        игры %побед болельщики
weights = [[0.1, 0.1, -0.3],  # травмы
           [0.1, 0.2, 0.0],  # победа?
           [0.0, 1.3, 0.1]]  # печаль?

toes = [8.5, 9.5, 9.9, 9.0]  # Среднее число игр, сыгранных игроками
wlrec = [0.65, 0.8, 0.8, 0.9]  # Доля побед
nfans = [1.2, 1.3, 0.5, 1.0]  # Число болельщиков

hurt = [0.1, 0.0, 0.0, 0.1]  # Травмы
win = [1, 1, 0, 1]  # Победы
sad = [0.1, 0.0, 0.1, 0.2]  # Моральное состояние игроков

alpha = 0.01

input = [toes[0], wlrec[0], nfans[0]]  # Входы
true = [hurt[0], win[0], sad[0]]  # Выходы

pred = neural_network(input, weights)

error = [0, 0, 0]
delta = [0, 0, 0]

for i in range(len(true)):
    error[i] = (pred[i] - true[i]) ** 2
    delta[i] = pred[i] - true[i]

weights_deltas = outer_prod(input, delta)
for i in range(len(weights)):
    for j in range(len(weights[i])):
        weights[i][j] -= alpha * weights_deltas[i][j]
print(weights)
