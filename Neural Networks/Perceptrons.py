

### Ishmael Rogers
## Infinitely Deep Robotics Group 
## 2018 

#The following program implements the perceptron trick given previous data and makes a prediction about new data


#imports section

import numpy as np
import math 


#Essential functions

# defines a function that returns 1 if t is greater than or equal to zero 
#returns zero otherwizs
def stepFunction(t): 
	if t >= 0:
		return 1
	return 0
#The prediction function performs the previously defined stepFunction on the the matrix defined by the weights and biases 

def prediction(X, W, b):
	return stepFunction((np.matmul(X, W) + b )[0])

#softmax function z is either a 1 or 2 dimentional logit. 
#logit is a row with 3 numbers
def softmax(z):
    """Compute softmax values for each sets of scores in z."""
    
    return np.exp(z) / np.sum(np.exp(z), axis=0)


####################################################

# This is th perceptron step covered in the readMe.md file. 


def perceptronStep(X, y, W, b, learn_rate = 0.01):

	for i in range(len(X)):
		#the prediction is based on input i, the weights array and bias
		y_hat = prediction(X[i], W, b)
		#check the label vs the prediction 
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
