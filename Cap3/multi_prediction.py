"""
#basic version of multi_prediction function(one input -> multi outputs)#
@author: <OKEAN>
DATE: 2024/9/13

weights = [0.3, 0.2, 0.9]

def ele_mul(number, vector):
    output = [0, 0, 0]
    assert(len(output) == len(vector))
    for i in range(len(vector)):
        output[i] = number*vector[i]
    return output

def neural_network(input, weights):
    pred = ele_mul(input, weights)
    return pred

wlrec = [0.65, 0.8, 0.8, 0.9]
input = wlrec[0]
pred = neural_network(input, weights)

print(pred)
"""

'''
#multi_prediction function(multiple inputs -> multiple outputs)
weights = [[0.1, 0.1, -0.3],  # hurt?
           [0.1, 0.2, 0.0],  # win?
           [0.0, 1.3, 0.1]]  # sad?


def w_sum(a,b):  # calculating the dot product of two vectors
    assert(len(a) == len(b))
    output = 0
    for i in range(len(a)):
        output += (a[i]*b[i])
    return output


def vect_mat_mult(vect,matrix):  # multiplying a vector by a matrix
    assert(len(vect) == len(matrix))
    output = [0, 0, 0]

    for i in range(len(vect)):
        output[i] = w_sum(vect,matrix[i])
    return output

def neural_network(input, weights):
    pred = vect_mat_mult(input, weights)
    return pred

toes = [8.5, 9.5, 9.9, 9.0]
wlrec = [0.65, 0.8, 0.8, 0.9]
nfans = [1.2, 1.3, 0.5, 1.0]

input = [toes[0], wlrec[0], nfans[0]]
pred = neural_network(input, weights)

print(pred)
'''

'''
#use Numpy to do multiple prediction with hidden layers#
import numpy as np
ih_wgt = np.array([[0.1, 0.2, -0.1],
                   [-0.1, 0.1, 0.9],
                   [0.1, 0.4, 0.1]]).T

hp_wgt = np.array([[0.3, 1.1, -0.3],
                   [0.1, 0.2, 0.0],
                   [0.0, 1.3, 0.1]]).T

weights = [ih_wgt, hp_wgt]

def neural_network(input, weights):
    hid = input.dot(weights[0])
    pred = hid.dot(weights[1])
    return pred

toes = [8.5, 9.5, 9.9, 9]
wlrec = [0.65, 0.8, 0.8, 0.9]
nfans = [1.2, 1.3, 0.5, 1.0]

input = np.array([toes[0], wlrec[0], nfans[0]])

pred = neural_network(input, weights)
print(pred)
'''
