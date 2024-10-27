"""
#basic version of one predict function#
@author: <OKEAN>
DATE: 2024/9/13

def w_sum(a,b):
    assert (len(a) == len(b))
    output = 0

    for i in range(len(a)):
        output += (a[i]*b[i])
    return output

weight = [0.1, 0.2, 0]

def neural_network(input,weight):
    prediction = w_sum(input,weight)
    return prediction

toes = [8.5, 9.5, 10, 9]
wirec = [0.65, 0.8, 0.8, 0.9]
nfans = [1.2, 1.3, 0.5, 1.0]

input = [toes[0], wirec[0], nfans[0]]
pred = neural_network(input,weight)
print(pred)
"""

"""
#one predict function with NumPy#

import numpy as np
weights = np.array([0.1, 0.2, 0])

def neural_network(input,weights):
    pred = input.dot(weights)
    return pred

toes = np.array([8.5, 9.5, 10, 9])
wirec = np.array([0.65, 0.8, 0.8, 0.9])
nfans = [1.2, 1.3, 0.5, 1.0]

input = np.array([toes[0], wirec[0], nfans[0]])

pred = neural_network(input,weights)
print(pred)
"""