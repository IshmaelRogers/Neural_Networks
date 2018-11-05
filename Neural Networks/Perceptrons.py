

### Ishmael Rogers
#imports 

import numpy as np
import math 




#Functions

def stepFunction(t): 
	if t >= 0:
		return 1
	return0

def prediction(X, W, b):
	return stepFunction((np.matmul(X, W) + b )[0])

#softmax function z is either a 1 or 2 dimentional logit. 
#logit is a row with 3 numbers
def softmax(z):
    """Compute softmax values for each sets of scores in z."""
    
    return np.exp(z) / np.sum(np.exp(z), axis=0)


####################################################

# Perceptron step 

def perceptronStep(X, y, W, b, learn_rate = 0.01):

	for i in range(len(X)):
		#prediction based on input i, the weights array and bias
		y_hat = prediction(X[i], W, b)
		#if the point is classified as positive, but has the negative label
		if y[i] - y_hat == 1:
			W[0] += X[i][0] * learn_rate
			W[1] += X[i][0] * learn_rate
			b += learn_rate
		#if the point is classified as negative, but has the positive label 
		elif y[i] - y_hat == -1:
			W[0] -= X[i][0] * learn_rate
			W[1] -= X[i][1] * learn_rate
			b -= learn_rate

	return W, b 

#################################################
