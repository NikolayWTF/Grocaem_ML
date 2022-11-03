import numpy as np


def neural_network(inp, weigh):
    pred = vect_mat_mul(inp, weigh)
    return pred


def w_sum(a, b):
    assert len(a) == len(b)
    output = 0
    for i in range(len(a)):
        output += a[i] * b[i]
    return output


def vect_mat_mul(vect, matrix):
    assert len(vect) == len(matrix)
    output = [0, 0, 0]

    for i in range(len(vect)):
        output[i] = w_sum(vect, matrix)

    return output


#                     Игр | Побед | Болельщики
weights = np.array([[0.1, 0.1, 0.0],    # Травмы?
                    [0.1, 0.2, 1.3],    # Победы?
                    [-0.3, 0.0, 0.1]])  # Грусть?

toes = np.array([8.5, 9.5, 9.9, 9.0])
wlrec = np.array([0.65, 0.8, 0.8, 0.9])
nfans = np.array([1.2, 1.3, 0.5, 1.0])

my_inp = np.array([toes[0], wlrec[0], nfans[0]])

predict = neural_network(my_inp, weights)
print(predict)
